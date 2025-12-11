# backend/app/services/pipeline.py

from file_scanner import FileScannerService
from file_loader import FileLoaderService
from chunker import ChunkerService
from embedding_service import EmbeddingService
from vector_store import VectorStore


class IngestionPipeline:
    def __init__(self, base_dir="../../", dim=384):
        self.base_dir = base_dir

        # Day 3 components
        self.scanner = FileScannerService(base_dir)
        self.loader = FileLoaderService()
        self.chunker = ChunkerService()

        # Day 4 component (embeddings)
        self.embedder = EmbeddingService()

        # Day 5 component (vector store)
        self.vector_store = VectorStore(dim)

    def run(self):
        """
        Full ingestion pipeline: scan → load → chunk → embed → store.
        Returns:
            files: list of scanned files
            all_chunks: all text chunks generated
        """
        files = self.scanner.scan()
        all_chunks = []

        for file in files:
            print(f"\n📄 Processing file: {file}")

            text = self.loader.load_file(file)
            chunks = self.chunker.chunk(text)

            print(f" - Found {len(chunks)} chunks")

            for idx, chunk in enumerate(chunks):
                vector = self.embedder.embed(chunk)

                metadata = {
                    "file_path": str(file),
                    "chunk_index": idx,
                    "total_chunks": len(chunks),
                    "preview": chunk[:120]
                }

                self.vector_store.add(vector, metadata)

            all_chunks.extend(chunks)

        return files, all_chunks

    def search(self, query, top_k=5):
        """
        Run semantic search using FAISS.
        Returns: list of {distance, metadata}
        """
        print("\n🔍 Running semantic search…")

        query_vector = self.embedder.embed(query)

        # ⚠️ NO MORE keyword argument — pure positional.
        results = self.vector_store.search(query_vector, top_k)

        return results
