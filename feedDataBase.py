# Backend - store all user ID

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createTable import *      # to enable us to import all of the data here into createTable.py

engine = create_engine('sqlite:///tutorialABC.db', echo = True)

#Create session
Session = sessionmaker(bind=engine)
session = Session()

firstUser = UserABC("admin" , "1111")
session.add(firstUser)

secondUser = UserABC("amami", "spaghetti")
session.add(secondUser)

thirdUser = UserABC("Dwi", "do we")
session.add(thirdUser)

#Store new user into database
session.commit() 
