# backend/app/services/test_pipeline.py

from pipeline import IngestionPipeline

print("\n=== 🧪 CodeSeer Day 5 Pipeline Test ===")

# point to a small test folder (relative to this file)
pipeline = IngestionPipeline(base_dir="./sample_code")

print("\n🚀 Starting ingestion pipeline...\n")

files, chunks = pipeline.run()

print("\n--- Ingestion Complete ---")
print(f"Total files processed: {len(files)}")
print(f"Total chunks created: {len(chunks)}")

print("\n🔍 Testing search...\n")
results = pipeline.search("config loader")

print("\n--- Search Results ---\n")
if not results:
    print("No results found (index may be empty).")
else:
    for r in results:
        # r is a dict: {"distance": <float>, "metadata": <dict>}
        distance = r.get("distance")
        metadata = r.get("metadata")
        print(f"Distance: {distance}")
        print(f"Metadata: {metadata}\n")
