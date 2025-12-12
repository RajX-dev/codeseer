# backend/app/services/search_service.py

from pipeline import IngestionPipeline


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
        return self.pipeline.search(query, top_k)
