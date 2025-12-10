from file_scanner import FileScannerService
from file_loader import FileLoaderService
from chunker import ChunkerService
from embedding_service import EmbeddingService
from vector_store import VectorStore

print("\n--- CodeSeer Day 4 Testing ---")

# Initialize services
scanner = FileScannerService("../../")
loader = FileLoaderService()
chunker = ChunkerService()
embedder = EmbeddingService()

# Pick test file
files = scanner.scan()
test_file = next(str(f) for f in files if str(f).endswith((".py", ".js")))

print(f"Testing on: {test_file}")

# Load + chunk
text = loader.load_file(test_file)
chunks = chunker.chunk(text)

print(f"Total chunks: {len(chunks)}")

# Create vector store
vector_dim = 384
store = VectorStore(dim=vector_dim)

# Embed all chunks
for idx, chunk in enumerate(chunks):
    vec = embedder.embed(chunk)
    meta = {
        "file_path": test_file,
        "chunk_index": idx,
        "total_chunks": len(chunks),
    }
    store.add(vec, meta)

print("Embeddings added to vector store.")

# Semantic search test
query = "function definition"  # you can change this
query_vec = embedder.embed(query)

results = store.search(query_vec, k=3)

print("\n--- Search Results ---")
for r in results:
    print(f"Distance: {r['distance']:.3f}")
    print(f"Metadata: {r['metadata']}")
