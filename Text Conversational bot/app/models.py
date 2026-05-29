from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from datetime import datetime
from app.database import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    role = Column(String)
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class UserMemory(Base):

    __tablename__ = "user_memory"

    id = Column(Integer, primary_key=True)

    user_id = Column(String, unique=True)

    summary = Column(Text)



