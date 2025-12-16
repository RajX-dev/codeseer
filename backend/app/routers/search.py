# backend/app/routers/search.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["search"])

# Create service ONCE
search_service = SearchService()


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


@router.post("/")
def semantic_search(req: SearchRequest):
    return search_service.search(req.query, req.top_k)
