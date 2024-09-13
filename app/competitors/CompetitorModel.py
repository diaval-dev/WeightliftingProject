from sqlalchemy.ext.declarative import declarative_base

from app.models.AuditBase import AuditBase
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class CompetitorsEntity(AuditBase):
    __tablename__ = 'competitors'

    competitor_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    department = Column(String)
    city = Column(String)
    competitor_name = Column(String)
    competitor_category = Column(String)
    competitor_type_document = Column(String)
    competitor_document = Column(String)
    competitor_phone = Column(String)
    competitor_birthdate = Column(Date)
    modality = Column(String)
    first_attempt = Column(Integer)
    second_attempt = Column(Integer)
    third_attempt = Column(Integer)
    total_olympic = Column(Integer)
    state = Column(String)
