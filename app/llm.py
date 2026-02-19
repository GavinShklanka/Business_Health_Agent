import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def get_llm():
    api_key = os.getenv("OPENAI_API_KEY")

    print("DEBUG OPENAI_API_KEY:", api_key)

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in environment.")

    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=api_key
    )
