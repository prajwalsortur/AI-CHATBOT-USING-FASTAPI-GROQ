# 🤖 Basic AI Chatbot
Absolutely. Let's keep **Project 1 = Simple AI Chatbot** only. No RAG, agents, tools, LangChain, LangGraph, MCP, etc. yet.

The goal is to first understand **how a real LLM-powered chatbot works from beginning to end**.

# 🤖 Project 1 — Simple AI Chatbot

### Project Goal

Build a simple chatbot where:

> **User → Chat UI → Backend → LLM → Backend → Chat UI → User**

The user types a question, the application sends it to an LLM, receives the response, and displays it.

---

# 1. What are we building?

A simple web-based chatbot.

Example:

```text
User:
What is Machine Learning?

        ↓

Chatbot Backend

        ↓

LLM
(Groq API)

        ↓

Response

        ↓

Chatbot UI

AI:
Machine Learning is a branch of AI...
```

That's it.

We are **not** making an AI agent yet.

---

# 2. Technologies we will use

| Technology              | Why we use it                              |
| ----------------------- | ------------------------------------------ |
| **Python**              | Backend programming                        |
| **FastAPI**             | Create our chatbot API                     |
| **Groq API**            | Connect our application to an LLM          |
| **LLM**                 | Generates the actual answers               |
| **HTML/CSS/JavaScript** | Simple chatbot interface                   |
| **Requests / HTTP**     | Communication between frontend and backend |
| **python-dotenv**       | Safely load API keys                       |
| **Git/GitHub**          | Version control and portfolio              |

### Important

The **LLM is the brain**.

Our Python/FastAPI application is basically the system that:

```text
receives message
      ↓
sends message to LLM
      ↓
gets response
      ↓
returns response to user
```

---

# 3. Basic Architecture

Our first architecture will be deliberately simple:

```text
                 ┌──────────────────┐
                 │      USER        │
                 └────────┬─────────┘
                          │
                          │ Message
                          ▼
                 ┌──────────────────┐
                 │   CHAT UI        │
                 │ HTML/CSS/JS      │
                 └────────┬─────────┘
                          │
                          │ HTTP Request
                          ▼
                 ┌──────────────────┐
                 │    FASTAPI       │
                 │    BACKEND       │
                 └────────┬─────────┘
                          │
                          │ API Request
                          ▼
                 ┌──────────────────┐
                 │    GROQ API      │
                 │      ↓           │
                 │      LLM         │
                 └────────┬─────────┘
                          │
                          │ AI Response
                          ▼
                 ┌──────────────────┐
                 │    FASTAPI       │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │     CHAT UI      │
                 └────────┬─────────┘
                          │
                          ▼
                        USER
```

---

# 4. Project Phases

We'll build it in **7 phases**.

```text
PHASE 1 → Project Setup
PHASE 2 → Understand the LLM API
PHASE 3 → Build FastAPI Backend
PHASE 4 → Connect Backend to LLM
PHASE 5 → Build Chat Interface
PHASE 6 → Connect Frontend + Backend
PHASE 7 → Testing + GitHub
```

Let's understand what happens in each phase.

---

# 🟢 PHASE 1 — Project Setup

### What happens?

We create our project and Python environment.

Structure:

```text
simple-chatbot/
│
├── backend/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

### Why?

We separate:

```text
frontend → what the user sees

backend → what happens behind the scenes
```

This is a standard approach for real applications.

---

# 🟢 PHASE 2 — Understand the LLM API

Before writing complicated code, we'll understand what we're actually calling.

Our application will send something like:

```text
"Explain Machine Learning"
```

to the LLM API.

The LLM processes it and returns:

```text
"Machine Learning is a branch of Artificial Intelligence..."
```

Conceptually:

```text
Our Application
      │
      │ Prompt
      ▼
   LLM API
      │
      │ Response
      ▼
Our Application
```

### Why Groq?

We're using Groq initially because it gives us a relatively simple way to access hosted LLMs without having to run a large model locally.

You already used Groq in your previous portfolio project, so this also gives you a chance to understand **what was actually happening behind that API call**.

---

# 🟢 PHASE 3 — Build the FastAPI Backend

Now we'll create our backend.

FastAPI will expose an endpoint such as:

```text
POST /chat
```

The frontend will send:

```json
{
    "message": "What is Python?"
}
```

The backend receives it.

### Why FastAPI?

Because we need something that can act as the **middle layer** between our UI and the LLM.

Without the backend:

```text
Frontend ─────────→ LLM API
```

But we don't want to expose our API key in frontend JavaScript.

Instead:

```text
Frontend
   ↓
FastAPI
   ↓
LLM API
```

This is much safer and closer to how production applications are structured.

---

# 🟢 PHASE 4 — Connect FastAPI to the LLM

This is the **core phase**.

Our backend will receive:

```text
User message
```

Then:

```text
FastAPI
   ↓
Create LLM request
   ↓
Send request to Groq
   ↓
LLM generates response
   ↓
Receive response
```

For example:

```text
User:
What is AI?

↓

FastAPI

↓

Groq

↓

LLM

↓

"Artificial Intelligence is..."

↓

FastAPI

↓

Frontend
```

### API Key

We'll keep the API key inside:

```text
.env
```

Example:

```text
GROQ_API_KEY=your_api_key
```

And `.env` will **not** be uploaded to GitHub.

---

# 🟢 PHASE 5 — Build the Chat Interface

Now we'll create the part the user actually sees.

Something like:

```text
┌──────────────────────────────────────┐
│          🤖 AI CHATBOT               │
├──────────────────────────────────────┤
│                                      │
│ AI: Hello! How can I help you?       │
│                                      │
│ You: What is Python?                 │
│                                      │
│ AI: Python is a programming...       │
│                                      │
├──────────────────────────────────────┤
│ Type your message...          [Send] │
└──────────────────────────────────────┘
```

We'll use:

### HTML

Creates the structure.

### CSS

Makes it look good.

### JavaScript

Makes it interactive.

For example:

```text
User clicks Send
        ↓
JavaScript gets message
        ↓
Sends HTTP request
        ↓
FastAPI
```

---

# 🟢 PHASE 6 — Connect Frontend + Backend

This is where everything comes together.

Suppose the user enters:

```text
What is Deep Learning?
```

JavaScript sends:

```text
POST /chat
```

to FastAPI.

FastAPI sends the message to the LLM.

LLM returns:

```text
Deep Learning is a subset of Machine Learning...
```

FastAPI returns it to JavaScript.

JavaScript displays it.

So the complete flow becomes:

```text
                USER
                  │
                  ▼
             CHAT UI
                  │
                  │ HTTP
                  ▼
              FASTAPI
                  │
                  │ API
                  ▼
               GROQ
                  │
                  ▼
                LLM
                  │
                  │ Response
                  ▼
              FASTAPI
                  │
                  ▼
             CHAT UI
                  │
                  ▼
                USER
```

🎯 **This is the most important thing you should understand from Project 1.**

---

# 🟢 PHASE 7 — Testing + GitHub

Once the chatbot works, we'll test things like:

### Normal question

```text
What is Python?
```

### Technical question

```text
Explain neural networks.
```

### Empty message

```text
""
```

### Long message

```text
...
```

### API failure

What happens if the LLM API doesn't respond?

We'll handle basic errors.

Then we'll clean the project and push it to GitHub.

---

# 5. What we are NOT using yet

This is important.

For **Project 1**, we deliberately won't use:

❌ LangChain
❌ LangGraph
❌ MCP
❌ RAG
❌ Vector databases
❌ Web search
❌ AI agents
❌ Tools
❌ Document processing
❌ Memory systems
❌ Multiple LLMs
❌ Complex frontend frameworks
❌ Fine-tuning

Why?

Because if we immediately use all of these, you may build something without understanding **what is actually happening underneath**.

---

# 6. What you should understand after Project 1

By the end, you should be able to explain this confidently:

### 1. What is an LLM?

The model that generates the chatbot's response.

### 2. What is an API?

A communication interface that allows our application to interact with another service.

### 3. What is Groq?

A platform/API through which we can access hosted LLMs.

### 4. What is FastAPI?

Our backend framework.

### 5. Why do we need a backend?

To handle application logic and keep secrets such as API keys away from the browser.

### 6. What is a prompt?

The input/instructions sent to the model.

### 7. What is a response?

The output generated by the model.

### 8. What is HTTP?

The communication mechanism between our frontend and backend.

### 9. What is JSON?

The structured format we'll use to send data between frontend and backend.

For example:

```json
{
    "message": "Hello"
}
```

### 10. What is the complete architecture?

You should be able to draw:

```text
User
 ↓
Frontend
 ↓
HTTP Request
 ↓
FastAPI
 ↓
Groq API
 ↓
LLM
 ↓
Response
 ↓
FastAPI
 ↓
Frontend
 ↓
User
```

---

# 7. Development Order

We should **not build everything at once**.

We'll work like this:

```text
STEP 1
Create project folder

        ↓

STEP 2
Create Python virtual environment

        ↓

STEP 3
Install required packages

        ↓

STEP 4
Test Groq API separately

        ↓

STEP 5
Create FastAPI server

        ↓

STEP 6
Create /chat endpoint

        ↓

STEP 7
Connect FastAPI → Groq

        ↓

STEP 8
Test backend using Swagger

        ↓

STEP 9
Create HTML interface

        ↓

STEP 10
Add CSS

        ↓

STEP 11
Add JavaScript

        ↓

STEP 12
Connect frontend → FastAPI

        ↓

STEP 13
Test complete chatbot

        ↓

STEP 14
Clean project

        ↓

STEP 15
GitHub + README
```

### And importantly:

Since you prefer learning **step-by-step**, we'll do **one step at a time**. I'll explain what each command/file does in simple terms, you run it, show me the output, and then we move to the next step.

**Project 1 = Simple Chatbot.** Once this works and you genuinely understand the flow, **Project 2 can start adding things like memory/RAG/tools/agents** rather than mixing everything into this first project.
