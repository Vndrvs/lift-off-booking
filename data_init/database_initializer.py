from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
import logging
import os

logging.getLogger('sqlalchemy').setLevel(logging.CRITICAL)

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)

    cities = relationship('City', back_populates='country')

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)

    airlines = relationship('Airline', back_populates='hq_city')
    country = relationship('Country', back_populates='cities')
    airports = relationship('Airport', back_populates='city')

class Airport(Base):
    __tablename__ = 'airports'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    code = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)

    city = relationship('City', back_populates='airports')
    origin_flights = relationship('Flight', foreign_keys='Flight.origin_airport_id', back_populates='origin_airport')
    destination_flights = relationship('Flight', foreign_keys='Flight.destination_airport_id', back_populates='destination_airport')

class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = Column(DateTime, nullable=False)
    is_international = Column(Boolean, nullable=False)
    airline_id = Column(Integer, ForeignKey('airlines.id'), nullable=False)
    origin_airport_id = Column(Integer, ForeignKey('airports.id'), nullable=False)
    destination_airport_id = Column(Integer, ForeignKey('airports.id'), nullable=False)
    ticket_fare = Column(Float, nullable=False)
    passenger_limit = Column(Integer, nullable=False)

    origin_airport = relationship('Airport', foreign_keys=[origin_airport_id], back_populates='origin_flights')
    destination_airport = relationship('Airport', foreign_keys=[destination_airport_id], back_populates='destination_flights')
    airline = relationship('Airline', back_populates='flights')
    bookings = relationship('Booking', back_populates='flight')

class Airline(Base):
    __tablename__ = 'airlines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)

    hq_city = relationship('City', back_populates='airlines')
    flights = relationship('Flight', back_populates='airline')

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    booking_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    flight_id = Column(Integer, ForeignKey('flights.id'), nullable=False)
    first_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)

    flight = relationship('Flight', back_populates='bookings')

db_path = os.path.abspath(os.path.join(__file__, "..", "..", "flight_radar.db"))
engine = create_engine(f"sqlite:///{db_path}", echo=False)

def InitializeDatabase():
    print("Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables created.")