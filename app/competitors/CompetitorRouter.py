from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.competitors.CompetitorDto import CompetitorCreate
from app.competitors.CompetitorService import CompetitorService
from app.core.database import get_db
from app.utils.Utilities import ResponseMessages
from app.utils.jsend import JSendResponse

competitor_router = APIRouter()


@competitor_router.post("/")
def create_competitor(competitor: CompetitorCreate, db: Session = Depends(get_db)):
    service = CompetitorService(db)
    competitor_id = service.create_competitor(competitor)
    return JSendResponse(status="success", message=ResponseMessages.SUCCESS_QUERY, data=competitor_id)
