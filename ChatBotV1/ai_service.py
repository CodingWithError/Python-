from typing import List, Dict, Any
from groq import Groq
from config import (
    GROQ_API_KEY, 
    AI_MODEL, 
    AI_TEMPERATURE, 
    AI_MAX_TOKENS, 
    AI_TOP_P, 
    AI_FREQUENCY_PENALTY, 
    AI_PRESENCE_PENALTY,
    CONVERSATION_WINDOW_SIZE
)


client = Groq(api_key=GROQ_API_KEY)


def get_conversation_window(conversation: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    non_system_messages = conversation[1:]  
    window = [conversation[0]] + non_system_messages[-CONVERSATION_WINDOW_SIZE:]
    return window


def generate_response(conversation: List[Dict[str, Any]]) -> str:
    window = get_conversation_window(conversation)
    
    try:
        chat_completion = client.chat.completions.create(
            messages=window,
            model=AI_MODEL,
            temperature=AI_TEMPERATURE,
            max_tokens=AI_MAX_TOKENS,
            top_p=AI_TOP_P,
            frequency_penalty=AI_FREQUENCY_PENALTY,
            presence_penalty=AI_PRESENCE_PENALTY,
        )
        return chat_completion.choices[0].message.content
    except Exception as exc:
        return f"Sorry, I ran into an error generating a response: {exc}"
