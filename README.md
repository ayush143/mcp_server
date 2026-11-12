# Multi-Server MCP Agent with LangGraph & Ollama

This project demonstrates how to connect a local Large Language Model (Qwen 3 via Ollama) to multiple external tools using the **Model Context Protocol (MCP)**. It uses LangChain and LangGraph to build an AI agent that can dynamically route user queries to the appropriate local server.

## Features
* **Local LLM Integration:** Powered by `qwen3:latest` running locally via Ollama.
* **Multi-Server MCP Client:** Connects to multiple MCP servers simultaneously using different transport layers.
* **Math Server (`stdio`):** A FastMCP server spawned as a child process to handle mathematical calculations.
* **Weather Server (`sse`):** A standalone FastMCP server running over HTTP/SSE to fetch weather data.
* **Agentic Routing:** Uses LangGraph's ReAct agent framework to automatically decide which tool to use based on the user's prompt.

## Prerequisites
Before running this project, ensure you have the following installed:
* [Python 3.10+](https://www.python.org/downloads/)
* [uv](https://docs.astral.sh/uv/) (Python package manager)
* [Ollama](https://ollama.com/) (Running locally on port 11434)

### Pull the Local Model
Make sure you have downloaded the Qwen 3 model in Ollama:
```bash
ollama run qwen3:latest

User:
"What is the weather in California?" or "What is (3+2)*12?"

    ↓
🧠 LangGraph Agent & Qwen 3 (AI Processing)

    ↓
Tool Selection (Math or Weather)

    ↓
🔌 MultiServerMCPClient

    ↓
⚙️ FastMCP Server Execution (stdio / sse)

    ↓
Return Result
