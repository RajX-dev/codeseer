from file_scanner import FileScannerService
from file_loader import FileLoaderService
from chunker import ChunkerService

# Initialize services
scanner = FileScannerService("../../")
loader = FileLoaderService()
chunker = ChunkerService()

# Scan all files
files = scanner.scan()
print(f"Found {len(files)} files")

# Pick first valid code file
test_file = next(
    str(f) for f in files
    if str(f).endswith((".py", ".js"))
)

print("Testing on:", test_file)

# Load selected file
text = loader.load_file(test_file)

# Chunk the file
chunks = chunker.chunk(text)

print("Chunks:", len(chunks))

# Print preview of first chunk
if chunks:
    print("\n--- First Chunk Preview ---")
    print(chunks[0][:300])
else:
    print("No chunks generated!")
