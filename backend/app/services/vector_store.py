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

    def search(self, query_vector, k=5):
        """
        Search k nearest vectors and return metadata + distances.
        """
        query_np = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_np, k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(self.metadata):
                results.append({
                    "distance": float(dist),
                    "metadata": self.metadata[idx]
                })
        return results

    def save(self, path="faiss.index"):
        faiss.write_index(self.index, path)

    def load(self, path="faiss.index"):
        self.index = faiss.read_index(path)
