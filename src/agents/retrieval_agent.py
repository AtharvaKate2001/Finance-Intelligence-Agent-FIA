from src.agents.base_agent import BaseAgent
from src.retrievers.sparse_retriever import SparseRetriever


class RetrievalAgent(BaseAgent):

    def __init__(self, embedder, vector_store, documents):
        super().__init__("RetrievalAgent")

        self.embedder = embedder
        self.vector_store = vector_store

        self.sparse_retriever = SparseRetriever(documents)

    def run(self, queries, top_k_per_query=2, max_chunks=6):
        """
        queries: list of query strings (original + expanded)
        """

        all_results = []

        for query in queries:


            embedding = self.embedder.embed(query)
            dense_results = self.vector_store.search(
                embedding,
                top_k=top_k_per_query
            )


            sparse_results = self.sparse_retriever.retrieve(
                query,
                top_k=top_k_per_query
            )


            for chunk in dense_results:
                all_results.append(chunk)


            for item in sparse_results:
                all_results.append(item["document"])


        unique_chunks = list(dict.fromkeys(all_results))


        return unique_chunks[:max_chunks]