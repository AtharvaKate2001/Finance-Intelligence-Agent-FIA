from src.agents.base_agent import BaseAgent
from src.llm.ollama_client import OllamaClient


class ResponseAgent(BaseAgent):
    def __init__(self):
        super().__init__("ResponseAgent")
        self.llm = OllamaClient(model="llama3")

    def run(self, policy_result: dict, retrieved_chunks=None) -> str:

        if not policy_result.get("allowed", False):
            return (
                "I can’t assist with that request. "
                "However, I can explain general financial concepts "
                "to help you make informed decisions."
            )

        user_query = policy_result["intent_data"]["original_query"]


        if retrieved_chunks:
            context_text = "\n\n".join(retrieved_chunks)

            prompt = f"""
You are a finance education assistant.

Use the provided context to answer the question.

Context:
{context_text}

User question:
{user_query}
"""


        else:
            prompt = f"""
You are a finance education assistant.

Answer the following finance question clearly and accurately.

Question:
{user_query}
"""

        return self.llm.generate(prompt, temperature=0.2)