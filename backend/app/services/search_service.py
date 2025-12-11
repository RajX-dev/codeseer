# backend/app/services/search_service.py

from embedding_service import EmbeddingService
from vector_store import VectorStore


class SearchService:
    def __init__(self, vector_store: VectorStore):
        self.embedder = EmbeddingService()
        self.vector_store = vector_store

    def search(self, query: str, top_k=5):
        print(f"\n🔍 Searching for: {query}")

        query_vector = self.embedder.embed(query)
        results = self.vector_store.search(query_vector, top_k=top_k)

        return results
