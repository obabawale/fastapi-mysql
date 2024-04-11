from app.db.base import Base
from sqlalchemy import Column, Integer, String


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(16), nullable=False)
    email = Column(String(16), nullable=False)
    first_name = Column(String(16), nullable=False)
    last_name = Column(String(16), nullable=False)
    password = Column(String(16), nullable=False)

