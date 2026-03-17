from src.agents.base_agent import BaseAgent
from src.llm.ollama_client import OllamaClient


class QueryExpansionAgent(BaseAgent):
    def __init__(self):
        super().__init__("QueryExpansionAgent")
        self.llm = OllamaClient(model="llama3")

    def run(self, user_query: str, num_variations: int = 3):
        prompt = f"""
You are a finance assistant helping improve search retrieval.

Generate {num_variations} alternative ways to ask the following question.
Keep them semantically similar but phrased differently.
Return each variation on a new line without numbering.

Question:
{user_query}
"""

        response = self.llm.generate(prompt, temperature=0.2)

        variations = [
            line.strip()
            for line in response.split("\n")
            if line.strip()
        ]

        return variations[:num_variations]
