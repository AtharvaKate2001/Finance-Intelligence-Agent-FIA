from src.rag.embedding_model import OllamaEmbeddingClient
from src.rag.document_loader import DocumentLoader
from src.rag.vector_store import VectorStore


def build_and_save_index():
    print("Building vector index...")

    embedder = OllamaEmbeddingClient()

    loader = DocumentLoader("G:/AI projects/Finance/data/finance_docs")
    documents = loader.load_documents()

    all_chunks = []
    all_embeddings = []

    for doc in documents:
        chunks = loader.chunk_text(doc["content"], chunk_size=150)

        for chunk in chunks:
            embedding = embedder.embed(chunk)
            all_chunks.append(chunk)
            all_embeddings.append(embedding)

    dimension = len(all_embeddings[0])
    vector_store = VectorStore(dimension)
    vector_store.add_embeddings(all_embeddings, all_chunks)

    vector_store.save("G:/AI projects/Finance/vector_db")

    print("Index built and saved successfully!")


if __name__ == "__main__":
    build_and_save_index()
