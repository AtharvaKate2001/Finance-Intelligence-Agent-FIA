from src.agents.base_agent import BaseAgent


class IntentAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntentAgent")

    def run(self, user_query: str) -> dict:


        query = user_query.lower()


        if any(word in query for word in ["buy", "sell", "invest", "stock", "crypto"]):
            intent = "investment_advice"

        elif any(word in query for word in ["budget", "save", "expense", "spend"]):
            intent = "budgeting"

        # Default category
        else:
            intent = "general_finance"

        return {
            "intent": intent,
            "original_query": user_query
        }
