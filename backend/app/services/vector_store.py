import faiss
import numpy as np


class VectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []  # parallel list to store chunk info

    def add(self, vector, meta):
        """
        Add embedding vector + metadata.
        """
        vector_np = np.array([vector]).astype("float32")
        self.index.add(vector_np)
        self.metadata.append(meta)

    def _distance_to_score(self, distance: float) -> float:
        """
        Convert FAISS L2 distance to a human-friendly relevance score.
        Higher score = more relevant.
        """
        return 1 / (1 + distance)

    def search(self, query_vector, k=5):
        """
        Search k nearest vectors and return metadata + distance + score.
        """
        query_np = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_np, k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(self.metadata):
                dist = float(dist)
                results.append({
                    "distance": dist,
                    "score": self._distance_to_score(dist),
                    "metadata": self.metadata[idx]
                })
        return results

    def save(self, path="faiss.index"):
        faiss.write_index(self.index, path)

    def load(self, path="faiss.index"):
        self.index = faiss.read_index(path)
