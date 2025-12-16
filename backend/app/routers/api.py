from fastapi import APIRouter
from app.routers.health import router as health_router
from app.routers.search import router as search_router

api_router = APIRouter()

# Feature routers
api_router.include_router(health_router)
api_router.include_router(search_router)

# Global/project-level route
@api_router.get("/info", tags=["Info"])
def project_info():
    return {
        "name": "CodeSeer",
        "version": "0.1.0",
        "description": "Distributed semantic code search engine"
    }
