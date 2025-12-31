from pydantic import BaseModel
from typing import Optional


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
    debug: bool = False


class SearchResult(BaseModel):
    rank: int
    score: float
    confidence: str
    file_path: str
    chunk_index: int
    preview: str
    reason: Optional[str] = None
