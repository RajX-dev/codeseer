from pydantic import BaseModel

class ChunkMetadata(BaseModel):
    file_path: str
    chunk_index: int
    total_chunks: int
    text: str
