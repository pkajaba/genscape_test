"""Models used for genscape tech test.
"""
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class DataPoint(Base):
    """Class representing Authors
    """
    __tablename__ = 'datapoints'
    id = Column(Integer, primary_key=True)
    identifier = Column(String)
    type = Column(String) # Enum might be better here
    # I would not probably better not to store temperature_c this,
    # but it's part of the task
    temperature_c = Column(Float)
    temperature_f = Column(Float)
    date = Column(DateTime)
