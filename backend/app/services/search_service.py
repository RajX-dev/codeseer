from app.services.pipeline import IngestionPipeline


class SearchService:
    """
    Thin service layer around the ingestion pipeline.
    """

    def __init__(self):
        self.pipeline = IngestionPipeline(base_dir="./sample_code")

        print("🚀 Initializing ingestion pipeline...")
        self.pipeline.run()
        print("✅ Ingestion ready.")

    def search(self, query: str, top_k: int = 5, debug: bool = False):
        # Fetch more results internally for better file-level aggregation
        raw_results = self.pipeline.search(query, top_k * 3)

        file_best = {}

        for r in raw_results:
            distance = r["distance"]
            score = 1 / (1 + distance)

            meta = r["metadata"]
            file_path = meta.get("file_path")

            if (
                file_path not in file_best
                or score > file_best[file_path]["score"]
            ):
                file_best[file_path] = {
                    "score": score,
                    "distance": distance,
                    "file_path": file_path,
                    "chunk_index": meta.get("chunk_index"),
                    "preview": meta.get("preview"),
                    "reason": "Semantic similarity between query and code content",
                }

        sorted_files = sorted(
            file_best.values(),
            key=lambda x: x["score"],
            reverse=True,
        )

        results = []

        for rank, r in enumerate(sorted_files[:top_k], start=1):
            score = r["score"]

            if score > 0.75:
                confidence = "high"
            elif score > 0.4:
                confidence = "medium"
            else:
                confidence = "low"

            result = {
                "rank": rank,
                "score": round(score, 3),
                "confidence": confidence,
                "file_path": r["file_path"],
                "chunk_index": r["chunk_index"],
                "preview": r["preview"],
                "reason": r["reason"],
            }

            if debug:
                result["debug"] = {
                    "raw_distance": round(r["distance"], 4),
                    "normalized_score": round(score, 4),
                }

            results.append(result)

        return results
