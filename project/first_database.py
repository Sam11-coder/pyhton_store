from sqlalchemy import create_engine, String,select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
data_base = "sqlite:///store.db"
engine = create_engine(data_base, echo=True)
Session = sessionmaker(bind=engine)
from first_database import engine
from first_models import Base

Base.metadata.create_all(engine)