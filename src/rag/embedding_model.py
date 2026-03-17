import requests


class OllamaEmbeddingClient:

    def __init__(self, model="nomic-embed-text", base_url="http://host.docker.internal:11434"):
        self.model = model
        self.api_url = f"{base_url}/api/embeddings"

    def embed(self, text: str):

        payload = {
            "model": self.model,
            "prompt": text
        }

        response = requests.post(self.api_url, json=payload, timeout=180)
        response.raise_for_status()

        result = response.json()

        return result["embedding"]