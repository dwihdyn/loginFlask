# BackEnd Controller (Business logic)

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

#for database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from createTable import *                   # bring in database
engine = create_engine('sqlite:///tutorialABC.db' , echo = True)


app = Flask(__name__)

@app.route('/')                                      # DeliveryMan
def start():
    return render_template('login.html')



@app.route('/login' , methods = ['POST'])       # route to validate the login variable on login
def login():
    Session = sessionmaker(bind=engine)
    ses = Session()
    # below is orm (object relational mapper). is to convert python to sql. Read more here https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#common-filter-operators
    dataPulling = ses.query(UserABC).filter(UserABC.usernameABC.in_([str(request.form['uSerName'])]), 
                                            UserABC.passwordABC.in_([str(request.form['pAssWord'])]))
    userDetail = dataPulling.first()

    if userDetail:
        session['logged_in'] = True
        return render_template('home.html')
    else:
        return render_template('home.html')





    # old version 
    # if request.form['pAssWord'] == '1111' and request.form['uSerName'] == 'admin':
    #     session['logged_in'] = True
    #     return render_template('home.html')         # was forgotten to state the destination html, if password is right
    # else:
    #     return render_template('home.html')







@app.route('/logout' , methods = ['POST'])
def logout():
    session['logged_in'] = False
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registeration.html')

@app.route('/registerDone', methods = ['POST'])
def registerDone():
    # store thoe newly input data into database. ANYTHING RELATED TO DATABASE must use sessionmaker
    Session = sessionmaker(bind=engine)         
    ses = Session()   
    newUser = UserABC( str(request.form['uSerName']) , str(request.form['pAssWord']))
    ses.add(newUser)
    ses.commit()
    return render_template('login.html')

@app.route('/seeAllUsers')      # dont need method = POST bc we are not submitting any data
def seeAllUsers():
    Session = sessionmaker(bind=engine)
    ses = Session()
    return render_template('listOfUsers.html', listUsers = ses.query(UserABC).all() )  #specify which table you want to see by ses.query(UserABC)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug = True, host = '0.0.0.0' , port = 4000) 