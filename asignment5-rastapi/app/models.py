from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, autoincrement=True,primary_key = True, nullable= False)
    name = Column(String, nullable = False)
    department = Column(String, nullable = False)

