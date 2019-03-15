# Backend model to create tutorialABC.db.
# the main purpose of this is to JUST create an empty table, waiting to be feed by data 

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///tutorialABC.db', echo = True)
Base = declarative_base()               # creating schema and name it 'Base'

class UserABC(Base):                    # creating table and name it "List_of_users"
    __tablename__ = "List_of_users"

    idABC = Column(Integer, primary_key = True)         # set id as Primary Key column
    usernameABC = Column(String)
    passwordABC = Column(String)

    def __init__(self, usernameABC , passwordABC):
        self.usernameABC = usernameABC
        self.passwordABC = passwordABC

Base.metadata.create_all(engine)
