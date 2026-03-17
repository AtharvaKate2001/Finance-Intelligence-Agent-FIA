# 💰 Finance Intelligence Agent (FIA)

A Dockerized multi-agent AI system that answers financial queries using Retrieval-Augmented Generation (RAG) and local LLMs.

---

## 🚀 Overview

Finance Intelligence Agent (FIA) is an AI-powered assistant designed to understand user queries related to finance and generate intelligent, context-aware responses.

The system combines:
- Multi-agent architecture
- Vector search (FAISS)
- Local LLM inference (Ollama)
- Interactive UI (Streamlit)

---

## 🧠 Problem Statement

Many users struggle to understand financial concepts such as inflation, mutual funds, and stock markets. Existing solutions either:

- Provide generic answers without context
- Lack personalization
- Depend heavily on internet APIs

---

## 💡 Solution

FIA solves this by:

- Understanding user intent using AI agents
- Retrieving relevant financial knowledge from a vector database
- Generating structured and meaningful responses using a local LLM

---

## 🏗️ Architecture

User (Streamlit UI)
↓
FastAPI Backend
↓
Intent Agent
→ Policy Agent
→ Retrieval Agent (FAISS + embeddings)
→ Response Agent
↓
Ollama (LLM)



---

## ⚙️ Tech Stack

- **Backend**: FastAPI  
- **Frontend**: Streamlit  
- **LLM**: Ollama (llama3)  
- **Embeddings**: nomic-embed-text  
- **Vector DB**: FAISS  
- **Containerization**: Docker  

---

## 📌 Features

- Multi-agent AI pipeline  
- Retrieval-Augmented Generation (RAG)  
- Local LLM (no external API dependency)  
- Interactive chat interface  
- Dockerized deployment  

---

## 🌍 Real-Life Applications

- Personal finance assistants  
- Banking and fintech chatbots  
- Financial education tools  
- Investment advisory systems  

---

## ⚠️ Important Notes

- The `vector_db/` folder is not included in the repository  
- It should be generated locally before running the system  

---

## 🚀 How to Run

### 1. Start Ollama locally

```bash
ollama pull llama3
ollama pull nomic-embed-text

### 2. Run Docker
docker compose up --build

### 3. Open UI
http://localhost:8501

💬 Example Query
What is inflation?

📈 Future Improvements

Chat history / memory
Streaming responses
Better UI (ChatGPT-style)
Cloud deployment
