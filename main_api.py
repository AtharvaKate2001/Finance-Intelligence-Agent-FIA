from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os
import pickle


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.agents.intent_agent import IntentAgent
from src.agents.policy_agent import PolicyAgent
from src.agents.response_agent import ResponseAgent
from src.agents.retrieval_agent import RetrievalAgent
from src.rag.embedding_model import OllamaEmbeddingClient
from src.rag.vector_store import VectorStore


app = FastAPI(title="Finance AI Backend")



embedder = OllamaEmbeddingClient()

vector_store = VectorStore(768)
vector_store.load("vector_db")
with open("vector_db/documents.pkl", "rb") as f:
    documents = pickle.load(f)

intent_agent = IntentAgent()
policy_agent = PolicyAgent()
retrieval_agent = RetrievalAgent(embedder, vector_store, documents)
response_agent = ResponseAgent()




class QueryRequest(BaseModel):
    query: str




@app.post("/ask")
def ask_finance_question(request: QueryRequest):

    user_input = request.query

    intent_output = intent_agent.run(user_input)
    policy_output = policy_agent.run(intent_output)

    retrieved_chunks = retrieval_agent.run([user_input], top_k_per_query=1)

    final_response = response_agent.run(policy_output, retrieved_chunks)

    return {
        "query": user_input,
        "response": final_response
    }
