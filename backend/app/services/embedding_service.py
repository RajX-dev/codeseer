from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str):
        """
        Returns a 384-dimensional embedding vector for the given text.
        """
        vector = self.model.encode(text)
        return vector
