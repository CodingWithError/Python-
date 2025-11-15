import os
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

_current_dir = Path(__file__).parent.resolve()
_default_path = _current_dir / "database" / "temp_conversation.json"

TEMP_JSON_PATH = os.getenv("TEMP_JSON_PATH")
if not TEMP_JSON_PATH:
    TEMP_JSON_PATH = str(_default_path)
else:
    env_path_obj = Path(TEMP_JSON_PATH)
    if env_path_obj.is_absolute():
        TEMP_JSON_PATH = str(env_path_obj)
    else:
        TEMP_JSON_PATH = str((project_root / env_path_obj).resolve())

print(f"[DEBUG] Using conversation file at: {TEMP_JSON_PATH}")

SYSTEM_MESSAGE = {
    "role": "system",
    "content": """You MUST always respond in English only, regardless of what language the user uses.

IMPORTANT RESPONSE GUIDELINES:
- Keep responses concise and focused (2-3 paragraphs maximum for general questions)
- Only provide detailed explanations with multiple points (4+ points) if the user explicitly asks for comprehensive coverage or a detailed breakdown
- For follow-up questions, refer back to your previous response accurately
- When the user asks about a specific numbered point, quote that exact point before explaining it
- Be precise and avoid confusion""",
}
AI_MODEL = "allam-2-7b"
AI_TEMPERATURE = 0.3
AI_MAX_TOKENS = 512
AI_TOP_P = 0.9
AI_FREQUENCY_PENALTY = 0.1
AI_PRESENCE_PENALTY = 0

CONVERSATION_WINDOW_SIZE = 12
