from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.models.AuditBase import AuditBase
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class CompetitorsEntity(AuditBase):
    __tablename__ = 'competitors'

    competitor_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    type_competence = Column(String)
    competitor_name = Column(String)
    competitor_gender = Column(String)
    competitor_category = Column(String)
    competitor_birthdate = Column(Date)
    competitor_university = Column(String)
    competitor_department = Column(String)
    total_olympic = Column(Integer)

    modalities = relationship("ModalitiesEntity")


class ModalitiesEntity(AuditBase):
    __tablename__ = 'modalities'

    modality_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    competitor_id = Column(UUID(as_uuid=True), ForeignKey('competitors.competitor_id'), nullable=False)
    modality_name = Column(String)
    first_attempt = Column(Integer)
    state_first_attempt = Column(String)
    second_attempt = Column(Integer)
    state_second_attempt = Column(String)
    third_attempt = Column(Integer)
    state_third_attempt = Column(String)
    total = Column(Integer)
