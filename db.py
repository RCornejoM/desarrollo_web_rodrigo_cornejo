from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def get_session():
    connection_string = "mysql+pymysql://user:password@localhost:3306/adopciones"
    engine = create_engine(connection_string, echo=True)
    return Session(engine)

