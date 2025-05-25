from sqlalchemy.orm import Session
from sqlalchemy import delete
from database_initializer import engine, Airline

with Session(bind=engine) as session:
    session.execute(delete(Airline))
    session.commit()
    print("Airlines table cleared.")