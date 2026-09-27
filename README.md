# AI CHATBOT USING FASTAPI & GROQ

A simple AI chatbot built with **HTML, CSS, JavaScript, FastAPI, and Groq API**.

The frontend provides a clean chat interface, while the FastAPI backend communicates with the Groq LLM and returns AI-generated responses. The chatbot also maintains **conversation history** during the current chat session.

## 🚀 Features

* 💬 Simple and responsive AI chat interface
* 🤖 Groq-powered AI responses
* ⚡ FastAPI backend
* 🧠 Conversation history
* ⌨️ Send messages using the Enter key
* 🔄 Loading indicator while waiting for AI responses
* 💭 Separate user and AI chat bubbles
* ⚠️ Basic error handling
* 🌐 HTML, CSS & JavaScript frontend
* 🔐 API key stored securely using `.env`
* 🔗 Frontend connected to FastAPI backend

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Uvicorn**
* **Groq API**
* **HTML**
* **CSS**
* **JavaScript**
* **python-dotenv**
* **Git & GitHub**

## 📁 Project Structure

```text
AI-CHATBOT-USING-FASTAPI-GROQ/
│
├── backend/
│   ├── main.py
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

## ⚙️ How It Works

```text
User
  ↓
Frontend Chat Interface
  ↓
JavaScript
  ↓
FastAPI Backend
  ↓
Groq API
  ↓
AI Response
  ↓
Conversation History
  ↓
Frontend
```

## 🧠 Conversation History

The chatbot keeps track of previous messages during the current conversation.

For example:

```text
User: My name is Prajwal.

AI: Nice to meet you, Prajwal!

User: What is my name?

AI: Your name is Prajwal.
```

This allows the chatbot to understand the context of previous messages instead of treating every message as completely separate.

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/prajwalsortur/AI-CHATBOT-USING-FASTAPI-GROQ.git
```

### 2. Open the project

```bash
cd AI-CHATBOT-USING-FASTAPI-GROQ
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn groq python-dotenv
```

### 6. Add your Groq API key

Create a `.env` file inside the `backend` folder:

```env
GROQ_API_KEY=your_api_key_here
```

### 7. Start the backend

From the project root:

```bash
python -m uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### 8. Open the frontend

Open:

```text
frontend/index.html
```

in your browser.

You can now start chatting with the AI.

## 🔐 Security

The Groq API key is stored in the `.env` file and should **never be uploaded to GitHub**.

Make sure your `.gitignore` contains:

```text
.env
.venv/
__pycache__/
```

Never share your API key publicly.

## 📌 Project Progress

### Version 1 — Completed

* Basic AI chatbot
* FastAPI backend
* Groq API integration
* Frontend chat interface

### Version 2 — Completed

* Conversation history
* Context-aware conversations
* Improved frontend interaction

### Version 3 — Completed

* Clear chat functionality
* Enter key to send messages
* Loading indicator
* User and AI message bubbles
* Basic error handling

## 🎯 Project Goal

The goal of this project is to build a simple understanding of how an AI-powered application works from **frontend → backend → LLM API → frontend response**.

It also serves as a foundation for gradually adding more advanced AI application features in future versions.

## 👨‍💻 Author

**Prajwal Sortur**

GitHub:
https://github.com/prajwalsortur

---

⭐ If you find this project useful, consider giving it a star!
