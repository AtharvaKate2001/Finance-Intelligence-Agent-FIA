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
ollama pull llama3
ollama pull nomic-embed-text

### 2. Run Docker
docker compose up --build

### 3. Open UI
http://localhost:8501

---

## 💬 Example Query
What is inflation?

Response from the assistance:

As a finance education assistant, I'd be happy to explain what inflation is.

Inflation is a fundamental concept in personal finance, and it's closely related to budgeting and financial planning.

Inflation refers to a sustained increase in the general price level of goods and services in an economy over a period of time. It's a measure of how quickly prices are rising. When there's inflation, the same amount of money can buy fewer goods and services than it could before.

For example, if the inflation rate is 2%, it means that prices are increasing by 2% over the course of a year. So, if you had 100 last year, you'd need 102 to buy the same goods and services this year.

Inflation can be caused by various factors, such as:

Increased demand for goods and services
Higher production costs
Changes in government policies or monetary policy
Global economic conditions
Inflation can have both positive and negative effects on the economy and individual finances. On the positive side, inflation can stimulate economic growth by encouraging spending and investment. On the negative side, high inflation can erode the purchasing power of your money, making it harder to save and budget effectively.

As a finance education assistant, I'd emphasize that it's essential to understand inflation and its impact on your financial decisions. This can help you make informed choices about your budget, investments, and long-term financial planning.

Do you have any follow-up questions about inflation or budgeting?

## 📈 Future Improvements

Chat history / memory

Streaming responses

Better UI (ChatGPT-style)

Cloud deployment
