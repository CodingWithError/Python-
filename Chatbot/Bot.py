from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")

print("Welcome to chat")
print("Please type what you want to ask the bot")
S=input("You: ").strip()
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=S
)
print(f"Bot: {response.text}")