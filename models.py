

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine("sqlite:///mydb.db",echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(bind=engine)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')
