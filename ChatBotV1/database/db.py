import os
from dotenv import load_dotenv
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in .env file")

from supabase import create_client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_conversation_to_supabase(title: str, conversation: list):
    payload = {"title": title, "content": conversation}
    try:
        res = supabase.table("conversations").insert(payload).execute()
        if hasattr(res, "error") and res.error:
            raise RuntimeError(f"Supabase error: {res.error}")
        return res
    except Exception as e:
        error_msg = str(e)
        if "Could not find the table" in error_msg:
            raise RuntimeError(
                f"Table 'conversations' does not exist in Supabase. "
                f"Please create the table with columns: 'title' (text) and 'content' (jsonb). "
                f"Original error: {error_msg}"
            )
        raise RuntimeError(f"Failed to save to Supabase: {error_msg}") from e


def get_conversation_history():
    try:
        res = supabase.table("conversations").select("id, title, created_at").order("created_at", desc=True).execute()
        if hasattr(res, "error") and res.error:
            raise RuntimeError(f"Supabase error: {res.error}")
        return res.data
    except Exception as e:
        raise RuntimeError(f"Failed to fetch conversation history: {str(e)}") from e


def load_conversation_by_id(conversation_id: int):
    try:
        res = supabase.table("conversations").select("*").eq("id", conversation_id).execute()
        if hasattr(res, "error") and res.error:
            raise RuntimeError(f"Supabase error: {res.error}")
        if not res.data:
            return None
        return res.data[0]
    except Exception as e:
        raise RuntimeError(f"Failed to load conversation: {str(e)}") from e


def update_conversation_in_supabase(conversation_id: int, title: str, conversation: list):
    payload = {"title": title, "content": conversation}
    try:
        res = supabase.table("conversations").update(payload).eq("id", conversation_id).execute()
        if hasattr(res, "error") and res.error:
            raise RuntimeError(f"Supabase error: {res.error}")
        return res
    except Exception as e:
        raise RuntimeError(f"Failed to update conversation in Supabase: {str(e)}") from e


def delete_conversation_by_id(conversation_id: int):
    try:
        res = supabase.table("conversations").delete().eq("id", conversation_id).execute()
        if hasattr(res, "error") and res.error:
            raise RuntimeError(f"Supabase error: {res.error}")
        return res
    except Exception as e:
        raise RuntimeError(f"Failed to delete conversation: {str(e)}") from e


def delete_all_conversations():
    try:
        res = supabase.table("conversations").select("id").execute()
        if hasattr(res, "error") and res.error:
            raise RuntimeError(f"Supabase error: {res.error}")        
        if res.data:
            for conv in res.data:
                supabase.table("conversations").delete().eq("id", conv["id"]).execute()
        
        return len(res.data) if res.data else 0
    except Exception as e:
        raise RuntimeError(f"Failed to delete all conversations: {str(e)}") from e
