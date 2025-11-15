from typing import List, Dict, Any
from database.db import (
    save_conversation_to_supabase, 
    get_conversation_history, 
    load_conversation_by_id, 
    update_conversation_in_supabase,
    delete_conversation_by_id,
    delete_all_conversations
)
from storage import (
    get_default_conversation,
    load_conversation_from_disk,
    persist_temp_conversation,
    reset_temp_conversation
)
from ai_service import generate_response


def finalize_conversation(conversation: List[Dict[str, Any]], title: str, conversation_id: int = None) -> None:
    if len(conversation) <= 1:
        print("No conversation to save. Exiting.")
        reset_temp_conversation()
        return
    
    try:
        if conversation_id:
            update_conversation_in_supabase(conversation_id, title, conversation)
            print("Conversation updated in Supabase.")
        else:
            save_conversation_to_supabase(title, conversation)
            print("Conversation saved to Supabase.")
    except Exception as exc:
        print(f"Failed to save conversation to Supabase: {exc}")
    finally:
        reset_temp_conversation()


def show_conversation_history() -> None:
    try:
        conversations = get_conversation_history()
        if not conversations:
            print("No previous conversations found.")
            print()
            return
        
        print("\n=== Conversation History ===")
        for conv in conversations:
            conv_id = conv.get("id")
            title = conv.get("title", "Untitled")
            created_at = conv.get("created_at", "Unknown date")
            print(f"ID: {conv_id} | Title: {title} | Created: {created_at}")
        print("===========================\n")
    except Exception as exc:
        print(f"Error fetching conversation history: {exc}")
        print()


def chat_loop(conversation: List[Dict[str, Any]], title: str, conversation_id: int = None) -> None:
    while True:
        user_input = input("You: ").strip()
        print()
        
        if user_input.lower() == "@exit":
            finalize_conversation(conversation, title, conversation_id)
            print("Conversation saved. Returning to main menu.")
            print()
            break

        conversation.append({"role": "user", "content": user_input})
        persist_temp_conversation(conversation)
        
        response = generate_response(conversation)
        
        conversation.append({"role": "assistant", "content": response})
        persist_temp_conversation(conversation)
        print(f"Bot: {response}")
        print()


def start_new_conversation() -> None:
    conversation = load_conversation_from_disk()    

    print()
    print("Welcome to the chat bot!")
    print("Bot uses multiple model APIs to generate responses.")
    print("The chat bot is not responsible for any actions taken based on its responses.")
    print("Type '@exit' to quit the chat bot.")
    print()
    
    title = ""
    while not title:
        title = input("Please enter a title for this conversation: ").strip()
        if not title:
            print("Title cannot be empty.")
    print()
    
    chat_loop(conversation, title)


def load_and_continue_conversation() -> None:
    show_conversation_history()
    
    conv_id_input = input("Enter the ID of the conversation to load (or '@cancel' to go back): ").strip()
    print()
    
    if conv_id_input.lower() == "@cancel":
        return
    
    try:
        conv_id = int(conv_id_input)
        conv_data = load_conversation_by_id(conv_id)
        
        if not conv_data:
            print(f"No conversation found with ID {conv_id}.")
            print()
            return
        
        title = conv_data.get("title", "Untitled")
        conversation = conv_data.get("content", [])
        
        if not isinstance(conversation, list):
            print("Invalid conversation format.")
            print()
            return
        
        # Ensure system message is at the start
        if not conversation or conversation[0].get("role") != "system":
            conversation = get_default_conversation() + conversation
        
        print(f"Loaded conversation: {title}")
        print("\n=== Previous Messages ===")
        for msg in conversation[1:]:  # Skip system message
            role = msg.get("role", "unknown")
            content = msg.get("content", "")
            if role == "user":
                print(f"You: {content}")
            elif role == "assistant":
                print(f"Bot: {content}")
            print()
        print("===========================\n")
        
        # Continue the conversation
        persist_temp_conversation(conversation)
        print("You can now continue this conversation. Type '@exit' to quit.\n")
        
        chat_loop(conversation, title, conv_id)
            
    except ValueError:
        print("Invalid ID. Please enter a valid number.")
        print()
    except Exception as exc:
        print(f"Error loading conversation: {exc}")
        print()


def delete_conversation() -> None:
    show_conversation_history()
    
    print("Enter the ID of the conversation to delete")
    print("Or type '@removeall' to delete all conversations")
    print("Or type 'cancel' to go back")
    
    user_input = input("Enter your choice: ").strip().lower()
    print()
    
    if user_input == "cancel":
        return
    
    if user_input == "@removeall":
        # Confirm delete all
        confirm = input("Are you sure you want to delete ALL conversations? Type '@confirm' to proceed: ").strip().lower()
        print()
        
        if confirm == "@confirm":
            try:
                count = delete_all_conversations()
                print(f"Successfully deleted {count} conversation(s).")
                print()
            except Exception as exc:
                print(f"Error deleting conversations: {exc}")
                print()
        else:
            print("Delete all cancelled.")
            print()
        return
    try:
        conv_id = int(user_input)        
        confirm = input(f"Are you sure you want to delete conversation ID {conv_id}? Type '@confirm' to proceed: ").strip().lower()
        print()
        
        if confirm == "@confirm":
            try:
                delete_conversation_by_id(conv_id)
                print(f"Successfully deleted conversation ID {conv_id}.")
                print()
            except Exception as exc:
                print(f"Error deleting conversation: {exc}")
                print()
        else:
            print("Delete cancelled.")
            print()
            
    except ValueError:
        print("Invalid input. Please enter a valid ID number, '@removeall', or 'cancel'.")
        print()
    except Exception as exc:
        print(f"Error: {exc}")
        print()
