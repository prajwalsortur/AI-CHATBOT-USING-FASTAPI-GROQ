from fastapi import FastAPI
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import os

load_dotenv("backend/.env")

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "Simple AI Chatbot Backend is running!"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    return {
        "response": response.choices[0].message.content
    }