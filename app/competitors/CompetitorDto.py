from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class Modalities(BaseModel):
    modality_name: Optional[str] = None
    first_attempt: Optional[int] = None
    state_first_attempt: Optional[str] = None
    second_attempt: Optional[int] = None
    state_second_attempt: Optional[str] = None
    third_attempt: Optional[int] = None
    state_third_attempt: Optional[str] = None
    total: Optional[int] = None


class CompetitorCreate(BaseModel):
    type_competence: str
    competitor_name: str
    competitor_gender: str
    competitor_category: str
    competitor_birthdate: date
    competitor_university: str
    competitor_department: str
    list_modalities: List[Modalities]
    total_olympic: int

    class Config:
        from_attributes = True
