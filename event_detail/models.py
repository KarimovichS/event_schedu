import uuid

from sqlalchemy.orm import relationship

from base.database import Base

from sqlalchemy import Column, Integer, String, VARCHAR, DateTime, UUID, ForeignKey


class EventDetail(Base):
    __tablename__ = 'event_detail'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    address = Column(VARCHAR, nullable=False)
    date = Column(DateTime, nullable=False)
    time = Column(DateTime, nullable=False)
    phone_number = Column(VARCHAR, nullable=False)
    recommended = Column(Integer, ForeignKey('recommended.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
