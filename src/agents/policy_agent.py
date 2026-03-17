from src.agents.base_agent import BaseAgent


class PolicyAgent(BaseAgent):
    def __init__(self):
        super().__init__("PolicyAgent")

    def run(self, intent_data: dict) -> dict:
        intent = intent_data.get("intent")


        if intent == "investment_advice":
            return {
                "allowed": False,
                "reason": "Providing specific investment advice is not allowed."
            }


        return {
            "allowed": True,
            "intent_data": intent_data
        }

