# 🤖 Simple AI Chatbot

A beginner-friendly AI chatbot built with **HTML, CSS, JavaScript, FastAPI, Python, and the Groq API**.

This project demonstrates how a web-based chatbot communicates with a backend API and uses a Large Language Model (LLM) to generate AI responses.

---

## ✨ Features

* 💬 Interactive chat interface
* 🤖 AI-generated responses using Groq
* ⚡ FastAPI backend
* 🌐 HTML, CSS, and JavaScript frontend
* 🔐 API key stored securely using environment variables
* 🔄 Real-time communication between frontend and backend
* 🧩 Simple architecture that can be extended with more AI features

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
Frontend
HTML + CSS + JavaScript
  │
  │ HTTP Request
  ▼
FastAPI Backend
  │
  │ API Request
  ▼
Groq API
  │
  │ AI Response
  ▼
FastAPI Backend
  │
  │ JSON Response
  ▼
Frontend
  │
  ▼
User
```

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### AI

* Groq API
* Large Language Model (LLM)

### Development Tools

* Git
* GitHub
* VS Code
* Python Virtual Environment

---

## 📁 Project Structure

```text
CHAT-BOT/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── ...
│
├── .gitignore
└── README.md
```

> `.env` should never be committed to GitHub because it contains the API key.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/prajwalsortur/CHAT-BOT.git
```

Navigate into the project:

```bash
cd CHAT-BOT
```

---

## 🐍 2. Create a Virtual Environment

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

---

## 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 4. Configure the Groq API Key

Create a `.env` file inside the `backend` folder.

Add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the value with your own Groq API key.

**Never upload your `.env` file to GitHub.**

---

## ▶️ 5. Start the Backend

From the `backend` folder:

```bash
uvicorn main:app --reload
```

The FastAPI server will run locally at:

```text
http://127.0.0.1:8000
```

FastAPI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## 🌐 6. Run the Frontend

Open the frontend `index.html` in your browser, or use the development setup included in the project.

Make sure the FastAPI backend is running before sending messages.

---

## 💬 How It Works

1. The user enters a message in the chatbot.
2. JavaScript sends the message to the FastAPI backend.
3. FastAPI receives the request.
4. The backend sends the message to the Groq API.
5. The LLM generates a response.
6. FastAPI sends the response back to the frontend.
7. The chatbot displays the AI response.

---

## 🧠 What I Learned

Through this project, I learned the basic workflow behind an AI-powered web application:

* How frontend and backend communicate
* How to create APIs using FastAPI
* How HTTP requests work
* How to connect an application to an LLM API
* How to use environment variables for API keys
* How to use Python virtual environments
* How to structure a simple full-stack AI application
* How to use Git and GitHub for version control

---

## 🔮 Future Improvements

This project is intentionally kept simple as **Version 1**.

Possible future improvements include:

* 🧠 Conversation memory
* 📄 RAG / document-based question answering
* 📎 File upload
* 🎙️ Voice input and output
* 🔐 User authentication
* 💾 Chat history
* 🧰 AI tools and function calling
* 📊 Conversation analytics
* 🌐 Deployment
* 🤖 More advanced agent capabilities

---

## 🎯 Project Goal

The goal of this project is to understand the fundamentals of building an **AI-powered chatbot from scratch**, starting with a simple implementation and gradually adding more advanced AI capabilities.

---

## 👨‍💻 Author

**Prajwal Sortur**

Electronics & Communication Engineering Graduate
Interested in:

* Data Science
* Artificial Intelligence
* Machine Learning
* Generative AI
* AI Engineering
* Data Analytics

### 🔗 Links

* GitHub: https://github.com/prajwalsortur
* Project Repository: https://github.com/prajwalsortur/CHAT-BOT

---

## ⭐ Future Roadmap

```text
Version 1
Simple AI Chatbot
       ↓
Version 2
Conversation Memory
       ↓
Version 3
RAG + Document Chat
       ↓
Version 4
AI Tools / Function Calling
       ↓
Version 5
Agentic AI Chatbot
```

---

## 📄 License

This project is created for learning and educational purposes.
