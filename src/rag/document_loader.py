import os


class DocumentLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_documents(self):
        documents = []

        for filename in os.listdir(self.data_path):
            if filename.endswith(".txt"):
                full_path = os.path.join(self.data_path, filename)

                with open(full_path, "r", encoding="utf-8") as f:
                    text = f.read()

                documents.append({
                    "filename": filename,
                    "content": text
                })

        return documents

    def chunk_text(self, text, chunk_size=300):
        chunks = []
        words = text.split()

        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)

        return chunks
