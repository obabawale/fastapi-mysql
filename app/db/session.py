import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

engine = create_engine(settings.MYSQL_DATABASE_URI)

Session = sessionmaker(autoflush=False, bind=engine)
