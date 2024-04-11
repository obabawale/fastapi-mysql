from app.db.base import Base
from sqlalchemy import Column, Integer, String


class Note(Base):

    __tablename__ = "note"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(16), nullable=False)
    content = Column(String(16))
