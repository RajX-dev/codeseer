from typing import List
from fastapi import APIRouter

from app.models.search import SearchRequest, SearchResult
from app.services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["search"])

search_service = SearchService()


@router.post("/", response_model=List[SearchResult])
def semantic_search(req: SearchRequest):
    return search_service.search(
        query=req.query,
        top_k=req.top_k,
        debug=req.debug,
    )
