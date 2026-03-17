import json
import re
from src.agents.base_agent import BaseAgent
from src.llm.ollama_client import OllamaClient


class ConfidenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("ConfidenceAgent")
        self.llm = OllamaClient(model="llama3")

    def evaluate(self, query: str, answer: str, context_chunks: list):
        context_text = "\n\n".join(context_chunks)

        prompt = f"""
You are evaluating the quality of an AI-generated financial answer.

User Question:
{query}

Retrieved Context:
{context_text}

AI Answer:
{answer}

Evaluate:

1. Is the answer fully supported by the context?
2. Does the answer introduce information not present in the context?
3. Rate grounding score from 0 to 10.
4. Rate answer completeness from 0 to 10.

Return ONLY valid JSON in this exact format:

{{
    "grounding_score": number,
    "completeness_score": number,
    "explanation": "short explanation"
}}
"""

        response = self.llm.generate(prompt, temperature=0.0)

        try:
            json_match = re.search(r"\{.*\}", response, re.DOTALL)

            if not json_match:
                raise ValueError("No JSON found in model response.")

            json_text = json_match.group()
            parsed = json.loads(json_text)

            grounding = float(parsed.get("grounding_score", 0))
            completeness = float(parsed.get("completeness_score", 0))

            overall_confidence = round(
                (grounding * 0.7 + completeness * 0.3) * 10,
                2
            )

            return {
                "grounding_score": grounding,
                "completeness_score": completeness,
                "overall_confidence": overall_confidence,
                "explanation": parsed.get("explanation", "")
            }

        except Exception:
            return {
                "grounding_score": 0,
                "completeness_score": 0,
                "overall_confidence": 0,
                "explanation": "Failed to parse confidence evaluation."
            }

    def enforce(self, confidence_dict: dict, threshold: float = 60):
        return confidence_dict.get("overall_confidence", 0) >= threshold
