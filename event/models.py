import uuid

from sqlalchemy.orm import relationship

from base.database import Base

from sqlalchemy import Column, Integer, String, VARCHAR, DateTime, UUID, ForeignKey


class Event(Base):
    __tablename__ = 'event'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(VARCHAR)
