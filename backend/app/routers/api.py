from fastapi import APIRouter
from app.routers.health import router as health_router

api_router = APIRouter()

api_router.include_router(health_router)

@api_router.get("/info", tags=["Info"])
def project_info():
    return {
        "name": "CodeSeer",
        "version": "0.1.0",
        "description": "Distributed semantic code search engine"
    }
