from fastapi import APIRouter

from app.competitors.CompetitorRouter import competitor_router

api_router = APIRouter()

api_router.include_router(competitor_router, prefix="/competitor", tags=["competitor"])
