from conversation_handler import (
    start_new_conversation,
    show_conversation_history,
    load_and_continue_conversation,
    delete_conversation
)


def main():
    print("Welcome!")
    print("Type '@start' to start the chat bot.")
    print("To check the previous conversations, type '@history'")
    print("To delete conversation, type '@delete'")
    print("To load the previous conversation, type '@load'")
    print("To exit the program, type '@exit'")
    print()
    
    while True:
        command = input("Enter command: ").strip().lower()
        print()
        
        if command == "@start":
            start_new_conversation()
        elif command == "@history":
            show_conversation_history()
        elif command == "@delete":
            delete_conversation()
        elif command == "@load":
            load_and_continue_conversation()
        elif command == "@exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please use '@start', '@history', '@delete', '@load', or '@exit'.")
            print()


if __name__ == "__main__":
    main()
