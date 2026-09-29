
# AI CHATBOT USING FASTAPI & GROQ

A simple AI chatbot built with **HTML, CSS, JavaScript, FastAPI, and Groq API**.

This project was created to understand the fundamental workflow of an **LLM-powered application** — from receiving a user's message in the frontend, sending it to a backend, communicating with an LLM through an API, and displaying the generated response back to the user.

The project also includes **conversation history**, allowing the chatbot to maintain context across multiple messages.

---

## 🚀 Project Overview

This project demonstrates how a basic LLM application works without using complex frameworks such as LangChain, LangGraph, RAG, vector databases, or AI agents.

The main goal is to understand the core communication flow:

```text
User
  ↓
Frontend
  ↓
FastAPI Backend
  ↓
Groq API
  ↓
LLM
  ↓
Generated Response
  ↓
FastAPI Backend
  ↓
Frontend
  ↓
User
```

---

## ✨ Features

* 💬 Simple AI chatbot interface
* 🤖 LLM integration using Groq API
* ⚡ FastAPI backend
* 🌐 HTML, CSS, and JavaScript frontend
* 🧠 Conversation history
* ⌨️ Send messages using the Enter key
* 🔄 Loading indicator while generating a response
* 💭 Separate user and AI message bubbles
* ⚠️ Basic error handling
* 🔐 API key stored using environment variables
* 📡 Frontend-to-backend API communication

---

## 🛠️ Technologies Used

| Technology    | Purpose                                    |
| ------------- | ------------------------------------------ |
| HTML          | Webpage structure                          |
| CSS           | User interface styling                     |
| JavaScript    | Frontend interaction and API communication |
| Python        | Backend programming                        |
| FastAPI       | Backend API framework                      |
| Groq API      | Communication with the LLM                 |
| LLM           | Generates natural-language responses       |
| Uvicorn       | Runs the FastAPI application               |
| python-dotenv | Loads environment variables                |

---

# 📁 Project Structure

```text
AI-CHATBOT-USING-FASTAPI-GROQ/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

> `.env` should remain local and should never be committed to GitHub.

---

# 🔄 How the Project Works

## Step 1 — User Enters a Message

The user types a question into the chatbot interface.

Example:

```text
What is machine learning?
```

The frontend captures this message using JavaScript.

---

## Step 2 — Frontend Sends the Message

JavaScript sends the user's message to the FastAPI backend through an HTTP request.

```text
Frontend
   ↓
HTTP Request
   ↓
FastAPI
```

The frontend does not communicate directly with the LLM.

---

## Step 3 — FastAPI Receives the Request

The FastAPI backend receives the user's message.

The backend acts as the bridge between the frontend and the Groq API.

```text
Frontend
    ↓
FastAPI
    ↓
Groq API
```

---

## Step 4 — Backend Sends the Request to Groq

FastAPI sends the required conversation information to the Groq API.

The request contains the user's message and, when applicable, previous conversation messages.

---

## Step 5 — Groq Communicates With the LLM

Groq provides access to the selected language model.

The LLM processes the provided input and generates a response.

Conceptually:

```text
User Message
     ↓
LLM
     ↓
Generated Tokens
     ↓
Generated Response
```

The LLM is responsible for generating the natural-language response.

---

## Step 6 — Groq Returns the Response

After the model generates its response, the response is returned through the Groq API to the FastAPI backend.

```text
LLM
 ↓
Groq API
 ↓
FastAPI
```

---

## Step 7 — FastAPI Returns the Response

FastAPI sends the generated response back to the frontend.

```text
FastAPI
   ↓
HTTP Response
   ↓
Frontend
```

---

## Step 8 — Frontend Displays the Response

JavaScript receives the response and displays it in the chatbot interface.

```text
AI:
Machine learning is a branch of artificial intelligence...
```

This completes one request-response cycle.

---

# 🧠 Conversation History

The chatbot also maintains conversation history.

For example:

```text
User:
My name is Prajwal.

AI:
Nice to meet you, Prajwal.

User:
What is my name?
```

The application can provide the previous messages as context when sending the new request to the LLM.

This allows the model to generate a response based on the conversation provided to it.

### Important Concept

The LLM does not automatically remember every previous interaction.

The application needs to provide the relevant previous messages as part of the request.

```text
Current Message
      +
Previous Messages
      ↓
    LLM
      ↓
Context-aware Response
```

---

# 🔐 Environment Variables

The Groq API key is stored in an environment file instead of being written directly into the source code.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

The `.env` file should be included in `.gitignore`.

Never upload API keys or other secrets to GitHub.

---

# ⚙️ Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/prajwalsortur/AI-CHATBOT-USING-FASTAPI-GROQ.git
```

Move into the project directory:

```bash
cd AI-CHATBOT-USING-FASTAPI-GROQ
```

---

## 2. Create a Virtual Environment

From the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 4. Configure the API Key

Create a `.env` file inside the `backend` folder:

```text
backend/
└── .env
```

Add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 5. Start the FastAPI Backend

Run:

```bash
uvicorn main:app --reload
```

The backend will start locally.

Example:

```text
http://127.0.0.1:8000
```

---

## 6. Run the Frontend

Open the frontend folder:

```text
frontend/
```

Open `index.html` using a local development server.

The frontend will communicate with the FastAPI backend.

---

# 🔌 Application Architecture

The project follows a simple client-server architecture:

```text
                USER
                  │
                  ▼
        ┌──────────────────┐
        │    FRONTEND      │
        │ HTML/CSS/JS      │
        └────────┬─────────┘
                 │
                 │ HTTP Request
                 ▼
        ┌──────────────────┐
        │     FASTAPI      │
        │     BACKEND      │
        └────────┬─────────┘
                 │
                 │ API Request
                 ▼
        ┌──────────────────┐
        │    GROQ API      │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │       LLM        │
        │ Language Model   │
        └────────┬─────────┘
                 │
                 ▼
        Generated Response
                 │
                 ▼
        ┌──────────────────┐
```
