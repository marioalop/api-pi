from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from infra.repositories.sql import constants as cts
from infra.repositories.sql.base import Base


class Character(Base):
    __tablename__: str = cts.CHARACTER_TABLE_NAME

    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(Float)
    mass = Column(Float)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(Integer)
