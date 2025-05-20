# Personal Agentic AI Chatbot

A **production-ready, modular AI chatbot** that leverages state-of-the-art language models (LLMs) from OpenAI and Groq, enhanced with real-time web search capabilities. Built with LangGraph, FastAPI, and Streamlit, this project offers an extensible platform for building, experimenting with, and deploying conversational AI agents.

---

## Table of Contents

- [Features](#features)
- [Project Layout](#project-layout)
- [Technical Architecture](#technical-architecture)
- [Prerequisites](#prerequisites)
- [Setup Guide](#setup-guide)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Multi-Provider LLM Support:** Seamlessly switch between OpenAI and Groq models (including Meta Llama and Mistral).
- **Web-Augmented AI:** Optionally enable real-time web search to supplement LLM knowledge.
- **Customizable Agent:** Define system prompts to tailor the chatbot’s behavior and personality.
- **Interactive Web UI:** User-friendly interface built with Streamlit.
- **API-First Backend:** FastAPI backend for robust, scalable, and modular integration.
- **Production-Ready:** Designed for reliability, extensibility, and easy deployment.

---

## Project Layout

### Phase 1 – Create AI Agent

1. **Setup API Keys** for Groq, OpenAI, and Tavily.
2. **Setup LLM & Tools:** Configure language models and web search tool.
3. **Setup AI Agent:** Integrate LLMs and enable optional search tool functionality.

### Phase 2 – Setup Backend (With FastAPI)

1. **Setup Pydantic Model:** For schema validation of API requests.
2. **Setup AI Agent from Frontend Request:** Connect backend logic to agent.
3. **Run App & Explore Swagger UI Docs:** Start the backend and review API endpoints.

### Phase 3 – Setup Frontend

1. **Setup UI with Streamlit:** Allow model provider/model selection, system prompt, and query input.
2. **Connect with Backend:** Communicate with backend via REST API.

---

## Technical Architecture

- **LangGraph ReAct Agents** – Orchestrate LLMs and tool usage.
- **FastAPI** – Backend API for handling requests.
- **Groq & OpenAI** – LLM providers (Meta Llama, Mistral, GPT-4, etc.).
- **Streamlit** – Frontend user interface.
- **LangChain** – Integration of tools and agent logic.
- **Uvicorn** – ASGI server for FastAPI.
- **Python** – Core programming language.
- **VS Code** – Recommended development environment.

---

## Prerequisites

- Python 3.9+
- API keys for:
  - OpenAI
  - Groq
  - Tavily (for web search)
- Git

---

## Setup Guide

### 1. Clone the Repository
```
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Set Up API Keys and Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-openai-key
GROQ_API_KEY=your-groq-key
TAVILY_API_KEY=your-tavily-key
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run the Backend (FastAPI)

Start the FastAPI server (default port: 9999):
```
uvicorn backend:app --reload --port 9999
```

- Access the API docs at: `http://localhost:9999/docs`

### 5. Run the Frontend (Streamlit)

In a new terminal, launch the Streamlit UI:
```
streamlit run frontend.py
```
- Open the provided local URL in your browser.

---

## Usage

1. **Open the Streamlit UI** in your browser.
2. **Configure the chatbot:**
   - Select LLM provider (OpenAI/Groq).
   - Choose a specific model (e.g., GPT-4o, Llama 3).
   - Enter a system prompt to define the agent’s behavior (optional).
   - Enable or disable web search augmentation.
   - Enter your query/message.
3. **Submit your query** and view the AI’s response.
4. **Review conversation history** and iterate as needed.

---

## Configuration

- **Models:** Choose from available LLMs (OpenAI, Groq, Meta Llama, Mistral).
- **Web Search:** Toggle web search augmentation for up-to-date responses.
- **System Prompt:** Customize the chatbot’s persona and expertise.

---

## Troubleshooting

- **API Key Errors:** Ensure all required API keys are set in your `.env` file.
- **Dependency Issues:** Reinstall dependencies and check Python version compatibility.
- **Connection Issues:** Confirm backend is running before launching the frontend.

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request with a clear description.

---

## License

This project is licensed under the MIT License.

---

**Build your own intelligent, web-augmented AI chatbot today—customizable, extensible, and ready for production!**




