import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


engine = create_engine(os.environ.get(
    "MYSQL_DATABASE_URI"))

Session = sessionmaker(autoflush=False, bind=engine)
