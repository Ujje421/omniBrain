# OmniBrain 🚀

## Overview

OmniBrain is a modular, extensible AI orchestration system designed to function as your own **AutoGPT / Jarvis-like assistant**. It combines multiple intelligent agents, a routing system, persistent memory, and backend infrastructure into a single powerful framework.

The goal of OmniBrain is simple: **help developers build autonomous AI systems that can think, act, remember, and create.**

---

## ✨ Core Features

### 🧠 Multi-Agent AI System

OmniBrain is built around a multi-agent architecture where each agent has a specific responsibility. Instead of relying on a single monolithic AI, tasks are delegated intelligently across specialized agents.

Examples:

* Planner Agent → Breaks down tasks
* Execution Agent → Performs actions
* Memory Agent → Stores and retrieves context
* File Agent → Generates files

---

### 🔀 AI Router

A smart routing layer determines **which agent should handle a request**.

* Understands user intent
* Dynamically selects the correct agent
* Enables scalable and modular AI workflows

---

### 📂 File Generation Agent

Generate real outputs directly from AI:

* Code files (Python, JS, etc.)
* Documents (Markdown, TXT)
* Structured data (JSON)

This makes OmniBrain not just conversational—but **actionable**.

---

### 🧬 Memory System

OmniBrain includes a persistent memory layer that allows it to:

* Remember past conversations
* Store structured knowledge
* Maintain long-term context

This is essential for building **stateful AI assistants**.

---

### 🌐 Basic Frontend

A lightweight frontend is included for:

* Interacting with agents
* Viewing outputs
* Testing workflows

Designed to be simple and easily customizable.

---

### 🐳 Docker Ready

Fully containerized for easy deployment:

* Consistent environment
* One-command startup
* Scalable infrastructure

---

## 🏗️ Architecture

```
User Input
   ↓
AI Router
   ↓
Selected Agent
   ↓
(Optional) Memory Access
   ↓
Execution / File Generation
   ↓
Response Output
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/your-repo/omnibrain.git
cd omnibrain
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Server

```
uvicorn main:app --reload
```

The server will start locally (typically on [http://127.0.0.1:8000](http://127.0.0.1:8000)).

---

## 🐳 Run with Docker

```
docker build -t omnibrain .
docker run -p 8000:8000 omnibrain
```

---

## 📁 Project Structure

```
omnibrain/
│
├── agents/            # Individual AI agents
├── router/            # AI routing logic
├── memory/            # Memory system
├── file_agent/        # File generation logic
├── frontend/          # Basic UI
├── main.py            # FastAPI entry point
└── requirements.txt
```

---

## 🔮 Vision

OmniBrain is designed to evolve into a **fully autonomous AI system** capable of:

* Planning complex tasks
* Executing multi-step workflows
* Learning from interactions
* Acting like a personal AI assistant (Jarvis-style)

The long-term vision is to empower developers to build:

* AI copilots
* Autonomous agents
* Business automation systems
* Personal productivity assistants

---

## 🧩 Use Cases

* Build your own AutoGPT system
* AI-powered developer assistant
* Workflow automation engine
* Smart chatbot with memory
* File/code generation platform

---

## ⚙️ Tech Stack

* FastAPI (Backend)
* Uvicorn (Server)
* Python (Core Logic)
* Docker (Deployment)

---

## 🤝 Contributing

Contributions are welcome!

* Fork the repo
* Create a feature branch
* Submit a pull request

---

## 📜 License

MIT License

---

## 💡 Final Note

OmniBrain is not just a chatbot backend — it’s a **foundation for building intelligent systems that think and act.**

Build your own Jarvis. 🧠⚡
