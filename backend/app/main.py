from fastapi import FastAPI
from app.core.config import settings
from app.routers.api import api_router

app = FastAPI(title=settings.PROJECT_NAME)

# Mount all routers under /api/v1
app.include_router(api_router, prefix=settings.API_V1)
