import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


engine = sqlalchemy.create_engine(os.environ.get(
    "MYSQL_DATABASE_URI", pool_pre_ping=True))

Session = sessionmaker(autoflush=False, bind=engine)
