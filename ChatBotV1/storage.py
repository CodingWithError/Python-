"""Handles local conversation storage operations"""
import copy
import json
from typing import List, Dict, Any
from pathlib import Path
from config import TEMP_JSON_PATH, SYSTEM_MESSAGE


def get_default_conversation() -> List[Dict[str, Any]]:
    return [copy.deepcopy(SYSTEM_MESSAGE)]


def ensure_temp_storage_dir() -> None:
    file_path = Path(TEMP_JSON_PATH)
    directory = file_path.parent
    directory.mkdir(parents=True, exist_ok=True)


def load_conversation_from_disk() -> List[Dict[str, Any]]:
    ensure_temp_storage_dir()
    file_path = Path(TEMP_JSON_PATH)
    
    if not file_path.exists():
        return get_default_conversation()
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if isinstance(data, list):
            conversation = data
        else:
            conversation = get_default_conversation()
    except (json.JSONDecodeError, OSError):
        conversation = get_default_conversation()
    
    # Ensure system message is at the start
    if not conversation or conversation[0].get("role") != "system":
        conversation = get_default_conversation() + conversation
    
    return conversation


def persist_temp_conversation(conversation: List[Dict[str, Any]]) -> None:
    ensure_temp_storage_dir()
    file_path = Path(TEMP_JSON_PATH)
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(conversation, f, ensure_ascii=False, indent=2)
    except OSError as exc:
        print(f"[warn] Failed to persist conversation to disk: {exc}")


def reset_temp_conversation() -> None:
    persist_temp_conversation(get_default_conversation())
