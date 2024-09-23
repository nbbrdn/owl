from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    description = Column(String)
    status = Column(String, default="open")
    created_at = Column(DateTime, server_default=func.now())
    resolved_at = Column(DateTime, nullable=True)
    time_spent = Column(Integer, nullable=True)
