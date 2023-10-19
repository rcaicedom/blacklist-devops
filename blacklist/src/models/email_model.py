from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from src.database.base import Base
from datetime import datetime, timezone

class BlackListModel(Base):
    __tablename__ = 'blacklist'
    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String(64), nullable=False, unique=True)
    reason =  Column(String(255))
    createdAt = Column(DateTime(), default=datetime.now(timezone.utc) )