from models import Base
from db import engine

Base.metadata.create_all(engine)
print("All tables have been created!")
