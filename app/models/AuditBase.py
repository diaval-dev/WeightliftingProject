from sqlalchemy import Column, DateTime, SmallInteger
from app.core.database import Base
from sqlalchemy.dialects.postgresql import UUID


class AuditBase(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))
    deleted_at = Column(DateTime(timezone=True))

    created_by = Column(UUID(as_uuid=True), nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_by = Column(UUID(as_uuid=True), nullable=True)

    status = Column(SmallInteger, nullable=False, default=1)