# backend/app/services/search_service.py

from app.services.pipeline import IngestionPipeline



class SearchService:
    """
    Thin service layer around the ingestion pipeline.
    """

    def __init__(self):
        # Load pipeline once
        self.pipeline = IngestionPipeline(base_dir="./sample_code")

        # Run ingestion ONCE at startup
        print("🚀 Initializing ingestion pipeline...")
        self.pipeline.run()
        print("✅ Ingestion ready.")

    def search(self, query: str, top_k: int = 5):
        raw_results = self.pipeline.search(query, top_k)

        enriched = []
        for rank, r in enumerate(raw_results, start=1):
            distance = r["distance"]
            score = 1 / (1 + distance)

            if score > 0.75:
                confidence = "high"
            elif score > 0.4:
                confidence = "medium"
            else:
                confidence = "low"

            meta = r["metadata"]

            enriched.append({
                "rank": rank,
                "score": round(score, 3),
                "confidence": confidence,
                "file_path": meta.get("file_path"),
                "chunk_index": meta.get("chunk_index"),
                "preview": meta.get("preview"),
            })

        return enriched
