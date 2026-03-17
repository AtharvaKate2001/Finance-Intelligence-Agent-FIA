from src.agents.base_agent import BaseAgent
from src.llm.ollama_client import OllamaClient


class ReRankingAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReRankingAgent")
        self.llm = OllamaClient(model="llama3")

    def score_chunk(self, query: str, chunk: str) -> float:
        prompt = f"""
You are evaluating how relevant a document chunk is to a user's question.

User Question:
{query}

Document Chunk:
{chunk}

Give a relevance score between 0 and 10.
Only return a number.
"""

        response = self.llm.generate(prompt, temperature=0.0)

        try:
            score = float(response.strip())
        except:
            score = 0.0

        return score

    def run(self, query: str, chunks: list, top_n: int = 3):
        scored_chunks = []

        for chunk in chunks:
            score = self.score_chunk(query, chunk)
            scored_chunks.append((chunk, score))


        scored_chunks.sort(key=lambda x: x[1], reverse=True)


        top_chunks = [chunk for chunk, _ in scored_chunks[:top_n]]

        return top_chunks
