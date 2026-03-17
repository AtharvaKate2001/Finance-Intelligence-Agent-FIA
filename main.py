import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from rag.embedding_model import OllamaEmbeddingClient
from rag.vector_store import VectorStore

from agents.intent_agent import IntentAgent
from agents.policy_agent import PolicyAgent
from agents.response_agent import ResponseAgent
from agents.retrieval_agent import RetrievalAgent


def initialize_system():
    print("Initializing Finance AI System...")

    embedder = OllamaEmbeddingClient()


    vector_store = VectorStore(768)
    vector_store.load("vector_db")


    intent_agent = IntentAgent()
    policy_agent = PolicyAgent()
    retrieval_agent = RetrievalAgent(embedder, vector_store)
    response_agent = ResponseAgent()

    print("System ready.\n")

    return intent_agent, policy_agent, retrieval_agent, response_agent


def run_cli():
    intent_agent, policy_agent, retrieval_agent, response_agent = initialize_system()

    print("Welcome to Finance AI Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break


        intent_output = intent_agent.run(user_input)
        policy_output = policy_agent.run(intent_output)

        retrieved_chunks = retrieval_agent.run(user_input, top_k=1)
        retrieved_chunks = [chunk[:800] for chunk in retrieved_chunks]


        final_response = response_agent.run(policy_output, retrieved_chunks)

        print("\nAI:", final_response)
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    run_cli()
