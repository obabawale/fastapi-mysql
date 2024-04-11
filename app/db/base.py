from sqlalchemy.ext import declarative

Base = declarative.declarative_base()
from app.models.user import User
from app.models.note import Note