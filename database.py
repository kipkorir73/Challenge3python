

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  

engine = create_engine("sqlite:///mydb.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(bind=engine)
