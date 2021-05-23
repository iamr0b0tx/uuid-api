from sqlalchemy import Column, Integer, String, func, DateTime
from .database import Base


class UUID(Base):
    __tablename__ = "uuid"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(128), index=True, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
