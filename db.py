from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

USER = "cc5002"
PASSWORD = "programacionweb"
HOST = "localhost"
PORT = 3306
DB = "tarea2"

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
