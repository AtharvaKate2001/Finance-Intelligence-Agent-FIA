import requests


class OllamaClient:
    def __init__(self, model="llama3", base_url="http://host.docker.internal:11434"):
        self.model = model
        self.api_url = f"{base_url}/api/generate"

    def generate(
        self,
        prompt: str,
        temperature: float = 0.3,
        stream: bool = False,
    ) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "temperature": temperature,
            "stream": False,
        }

        response = requests.post(self.api_url, json=payload, timeout=180)
        response.raise_for_status()

        result = response.json()

        if "response" not in result:
            raise ValueError(f"Ollama error: {result}")

        return result["response"]