from rank_bm25 import BM25Okapi


class SparseRetriever:

    def __init__(self, documents):
        self.documents = documents
        self.tokenized_docs = [doc.split() for doc in documents]
        self.bm25 = BM25Okapi(self.tokenized_docs)

    def retrieve(self, query, top_k=5):

        tokenized_query = query.split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )

        results = [
            {
                "document": self.documents[i],
                "score": scores[i]
            }
            for i in ranked_indices[:top_k]
        ]

        return results