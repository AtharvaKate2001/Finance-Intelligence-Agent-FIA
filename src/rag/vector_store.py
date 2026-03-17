import faiss
import numpy as np
import pickle
import os


class VectorStore:
    def __init__(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add_embeddings(self, embeddings, documents):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.documents.extend(documents)

    def search(self, query_embedding, top_k=3):
        query_vector = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)

        results = []

        for idx in indices[0]:
            results.append(self.documents[idx])

        return results

    def save(self, folder_path):
        os.makedirs(folder_path, exist_ok=True)

        faiss.write_index(self.index, os.path.join(folder_path, "index.faiss"))

        with open(os.path.join(folder_path, "documents.pkl"), "wb") as f:
            pickle.dump(self.documents, f)

    def load(self, folder_path):
        self.index = faiss.read_index(os.path.join(folder_path, "index.faiss"))

        with open(os.path.join(folder_path, "documents.pkl"), "rb") as f:
            self.documents = pickle.load(f)

