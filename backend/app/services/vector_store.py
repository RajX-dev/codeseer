import numpy as np
import faiss

class VectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add(self, vector, meta):
        vector_np = np.array([vector]).astype("float32")
        self.index.add(vector_np)
        self.metadata.append(meta)

    def search(self, query_vector, top_k=3):
        if len(self.metadata) == 0:
            return []

        query_np = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_np, top_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx == -1:
                continue

            results.append({
                "distance": float(dist),
                "metadata": self.metadata[idx]
            })

        return results
