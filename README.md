# 🤖 Basic AI Chatbot

### React • FastAPI • LLM API

> A simple AI-powered chatbot that allows users to send messages and receive intelligent responses from a Large Language Model (LLM).

---

## 📌 Overview

This project is a **basic LLM-powered chatbot** built to understand how modern AI chatbot applications work.

The application follows a simple flow:

```text
User
  ↓
React Chat Interface
  ↓
FastAPI Backend
  ↓
LLM API
  ↓
AI Response
  ↓
React Chat Interface
```

The main goal of this phase is to understand the **fundamentals of connecting a frontend, backend, and LLM** before adding advanced AI features.

---

## 🎯 Project Goals

* Understand how an LLM-powered chatbot works
* Build a simple chat interface
* Connect React with FastAPI
* Connect FastAPI with an LLM API
* Send user messages to the LLM
* Display AI-generated responses
* Learn basic API communication
* Secure API keys using environment variables

---

## 🧠 How It Works

### 1. User sends a message

The user enters a message in the chat interface.

```text
"Explain Machine Learning"
```

### 2. Frontend sends the message

React sends the user's message to the FastAPI backend.

```text
React
  ↓
POST /chat
```

### 3. Backend sends it to the LLM

FastAPI receives the message and sends it to the selected LLM API.

```text
FastAPI
   ↓
LLM API
```

### 4. LLM generates a response

The LLM processes the message and generates an answer.

```text
User Question
      ↓
     LLM
      ↓
AI Response
```

### 5. Response is displayed

The backend sends the response back to React, which displays it in the chat interface.

---

# 🏗️ Architecture

```text
                    ┌──────────────┐
                    │    USER      │
                    └──────┬───────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │  React Frontend  │
                 │                  │
                 │   Chat Interface │
                 └────────┬─────────┘
                          │
                          │ HTTP Request
                          ▼
                 ┌──────────────────┐
                 │  FastAPI Backend │
                 │                  │
                 │    /chat API     │
                 └────────┬─────────┘
                          │
                          │ API Request
                          ▼
                 ┌──────────────────┐
                 │     LLM API      │
                 │                  │
                 │   AI / "Brain"   │
                 └────────┬─────────┘
                          │
                          │ AI Response
                          ▼
                 ┌──────────────────┐
                 │  FastAPI Backend │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  React Frontend  │
                 └────────┬─────────┘
                          │
                          ▼
                    ┌──────────────┐
                    │    USER      │
                    └──────────────┘
```

---

# 🛠️ Tech Stack

### Frontend

* React
* Vite
* JavaScript
* CSS

### Backend

* Python
* FastAPI
* Uvicorn

### AI

* Large Language Model (LLM)
* LLM API

### Development

* Git
* GitHub
* VS Code
* Python Virtual Environment

---

# 📂 Project Structure

```text
AI-CHATBOT/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── App.css
│   │
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>

cd AI-CHATBOT
```

---

## 2. Create Python Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 4. Add API Key

Create a `.env` file inside the `backend` folder.

```env
LLM_API_KEY=your_api_key_here
```

> Never upload your `.env` file or API key to GitHub.

---

## 5. Start the Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

---

## 6. Start the Frontend

Open another terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

---

# 💬 Example

### User

```text
What is Artificial Intelligence?
```

### Chatbot

```text
Artificial Intelligence is a field of computer science
that focuses on creating systems capable of performing
tasks that normally require human intelligence.
```

---

# 🔄 Current Chatbot Flow

```text
User Message
     ↓
React
     ↓
FastAPI
     ↓
LLM API
     ↓
Generated Response
     ↓
FastAPI
     ↓
React
     ↓
User
``
```
