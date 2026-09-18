# AI CHATBOT USING FASTAPI & GROQ

A simple AI chatbot built with **HTML, CSS, JavaScript, FastAPI, and Groq API**.

The frontend allows users to send messages, while the FastAPI backend communicates with the Groq LLM and returns the AI-generated response.

## 🚀 Features

* 💬 Simple AI chat interface
* ⚡ FastAPI backend
* 🤖 Groq LLM integration
* 🌐 HTML, CSS & JavaScript frontend
* 🔐 API key stored securely using `.env`
* 🔗 Frontend connected to backend API

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Uvicorn**
* **Groq API**
* **HTML**
* **CSS**
* **JavaScript**
* **Git & GitHub**

## 📁 Project Structure

```text
AI-CHATBOT/
│
├── backend/
│   ├── main.py
│   └── .env
│
├── frontend/
│   └── index.html
│
├── .gitignore
└── README.md
```

## ⚙️ How It Works

```text
User
  ↓
Frontend
  ↓
FastAPI Backend
  ↓
Groq API
  ↓
AI Response
  ↓
Frontend
```

## 🧑‍💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/prajwalsortur/CHAT-BOT.git
```

### 2. Open the project

```bash
cd CHAT-BOT
```

### 3. Create and activate virtual environment

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn groq python-dotenv
```

### 5. Add your Groq API key

Create a `.env` file inside the `backend` folder:

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Start the backend

From the project root:

```bash
python -m uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### 7. Open the frontend

Open:

```text
frontend/index.html
```

in your browser and start chatting.

## 🔐 Security

The Groq API key is stored in the `.env` file and should **never be uploaded to GitHub**.

Make sure `.env` is included in `.gitignore`.

## 📌 Project Status

**Version 1 — Completed**

The basic AI chatbot is working with a frontend, FastAPI backend, and Groq-powered AI responses.

## 👨‍💻 Author

**Prajwal Sortur**

GitHub:
https://github.com/prajwalsortur

---

⭐ If you find this project useful, consider giving it a star!
