# 🤖 AI-Powered Intelligent Chatbot

### LLM • AI Agents • RAG • Tool Calling • LangChain • LangGraph • MCP

> An intelligent chatbot system designed to understand user queries, generate responses using Large Language Models, retrieve information from external knowledge sources, and interact with tools to perform useful tasks.

---

## 🚀 Overview

This project focuses on building a modern **AI chatbot** rather than a simple question-and-answer application.

The chatbot uses an **LLM as its reasoning engine** and can be extended with:

* 🧠 Large Language Models (LLMs)
* 🔧 Tool Calling
* 🌐 Web Search
* 📚 Retrieval-Augmented Generation (RAG)
* 🔗 LangChain
* 🕸️ LangGraph
* 🔌 MCP (Model Context Protocol)
* ⚡ FastAPI
* 🎨 React

The goal is to understand how modern AI assistants are designed and how an LLM can interact with external tools and knowledge.

---

## 🎯 Project Goals

* Understand how LLM-powered applications work
* Build a chatbot using an LLM API
* Implement conversation history
* Connect the chatbot with external tools
* Implement RAG for custom documents
* Allow the AI to decide when a tool is required
* Build multi-step AI workflows
* Understand agent architecture
* Explore MCP-based tool integration
* Create a production-style AI application

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       USER          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    React Frontend  │
                    │   Chat Interface    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │      Backend        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    AI Agent Layer   │
                    │                     │
                    │   LangChain /       │
                    │   LangGraph        │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
            ┌───────────────┐     ┌────────────────┐
            │     LLM       │     │     Tools      │
            │   The Brain   │     │                │
            └───────┬───────┘     │ • Web Search  │
                    │             │ • Calculator  │
                    │             │ • APIs        │
                    │             │ • Custom Tools│
                    │             └────────────────┘
                    │
                    ▼
             ┌──────────────┐
             │     RAG      │
             │              │
             │ Documents →  │
             │ Embeddings → │
             │ Vector DB    │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ Final Answer │
             └──────────────┘
```

---

# 🧠 How It Works

### 1. User asks a question

Example:

```text
What is machine learning?
```

The question is sent to the backend.

---

### 2. LLM receives the question

The **LLM acts as the brain** of the chatbot.

It understands the user's request and determines what kind of response is required.

---

### 3. The AI decides whether a tool is required

For example:

```text
User:
What is the weather in Bangalore?
```

The LLM can determine:

```text
I need a weather tool.
```

It then calls the appropriate tool.

---

### 4. Tool returns information

```text
Weather Tool
      ↓
Current weather data
      ↓
LLM
```

The LLM uses the returned information to generate the final response.

---

### 5. RAG handles private knowledge

If the user asks:

```text
What projects are mentioned in my resume?
```

The system can retrieve relevant information from uploaded documents.

```text
Documents
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Relevant Information
    ↓
LLM
    ↓
Answer
```

---

# 🔧 Tools

The chatbot can be extended with different tools.

### Example Tools

| Tool             | Purpose                            |
| ---------------- | ---------------------------------- |
| 🌐 Web Search    | Search current information         |
| 🧮 Calculator    | Perform calculations               |
| 📚 RAG           | Search private documents           |
| 🔌 APIs          | Retrieve external data             |
| 🗄️ Database     | Query structured data              |
| 🕐 Date/Time     | Get current date and time          |
| 🛠️ Custom Tools | Perform application-specific tasks |

---

# 📚 RAG Pipeline

Retrieval-Augmented Generation allows the chatbot to answer questions using information that is not part of the LLM's original training data.

```text
             Documents
                 │
                 ▼
          Text Extraction
                 │
                 ▼
             Chunking
                 │
                 ▼
            Embeddings
                 │
                 ▼
          Vector Database
                 │
                 ▼
          Similarity Search
                 │
                 ▼
       Relevant Context
                 │
                 ▼
                LLM
                 │
                 ▼
          Generated Answer
```

---

# 🕸️ Agent Workflow

The chatbot can use an agent-based workflow.

```text
User Query
    │
    ▼
   LLM
    │
    ├── Simple Question ──────► Answer
    │
    ├── Web Search Needed ────► Web Tool
    │                              │
    │                              ▼
    │                             LLM
    │
    ├── Document Needed ──────► RAG
    │                              │
    │                              ▼
    │                             LLM
    │
    └── Calculation Needed ───► Calculator
                                   │
                                   ▼
                                  LLM
                                   │
                                   ▼
                             Final Answer
```

---

# 🔌 MCP

This project also explores **Model Context Protocol (MCP)**.

MCP provides a standardized way for AI applications to connect models with external tools and data sources.

```text
                 AI Application
                       │
                       ▼
                      LLM
                       │
                       ▼
                  MCP Client
                       │
              ┌────────┼────────┐
              │        │        │
              ▼        ▼        ▼
           MCP Tool  MCP Tool  MCP Tool
              │        │        │
              ▼        ▼        ▼
            API      Database   Files
```

This helps demonstrate how modern AI systems can connect an LLM to external capabilities.

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

## AI / LLM

* Large Language Models
* LLM APIs
* Prompt Engineering
* Tool Calling
* AI Agents

## AI Frameworks

* LangChain
* LangGraph
* MCP

## RAG

* Embeddings
* Vector Database
* Document Processing
* Similarity Search

## Frontend

* React
* Vite
* JavaScript
* CSS

## Development Tools

* Git
* GitHub
* VS Code
* Python Virtual Environment
* REST APIs

---

# 📂 Project Structure

```text
AI-CHATBOT/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   │
│   ├── agent/
│   │   ├── agent.py
│   │   ├── prompts.py
│   │   └── workflow.py
│   │
│   ├── tools/
│   │   ├── web_search.py
│   │   ├── calculator.py
│   │   └── custom_tools.py
│   │
│   ├── rag/
│   │   ├── loader.py
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   └── vectorstore.py
│   │
│   ├── mcp/
│   │   └── mcp_client.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── data/
│   └── documents/
│
├── .gitignore
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>

cd AI-CHATBOT
```

---

## 2. Create Virtual Environment

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

## 4. Configure Environment Variables

Create a `.env` file inside the backend directory.

```env
LLM_API_KEY=your_api_key
```

Additional API keys can be added depending on the tools being used.

---

## 5. Start FastAPI

```bash
cd backend

uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

---

## 6. Start React Frontend

Open another terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 💬 Example Queries

### General Question

```text
What is artificial intelligence?
```

### Calculation

`
