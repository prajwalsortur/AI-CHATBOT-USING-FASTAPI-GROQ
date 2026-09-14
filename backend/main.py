from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv("backend/.env")

app = FastAPI()

api_key = os.getenv("GROQ_API_KEY")


@app.get("/")
def home():
    return {
        "message": "Simple AI Chatbot Backend is running!",
        "api_key_loaded": api_key is not None
    }