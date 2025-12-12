# backend/app/routers/search.py

from fastapi import APIRouter
from pydantic import BaseModel
from services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["search"])

# Create service ONCE
search_service = SearchService()


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


@router.post("/")
def semantic_search(req: SearchRequest):
    results = search_service.search(req.query, req.top_k)

    # Flatten response for API
    formatted = []
    for r in results:
        meta = r["metadata"]
        formatted.append({
            "distance": r["distance"],
            "file_path": meta.get("file_path"),
            "chunk_index": meta.get("chunk_index"),
            "preview": meta.get("preview"),
        })

    return formatted
