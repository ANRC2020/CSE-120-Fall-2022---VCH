from sqlalchemy.ext.declarative import declarative_base
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import sqlalchemy as db
from flask_admin.contrib.sqla import ModelView
import os
import pandas as pd
from TableSetup import Reset_Database
from flask_cors import CORS
import hashlib
import numpy as np

try:
    os.system("cls")
except:
    pass

# Returned Access Points for each of the Tables
patients, exams, doctors = Reset_Database()
app = Flask(__name__)

CORS(app)

engine = db.create_engine('sqlite:///VRDataBase.sqlite?check_same_thread=False')
conn = engine.connect()

# define declarative base
Base = declarative_base()

# reflect current database engine to metadata
metadata = db.MetaData(engine)
metadata.reflect()

# build your User class on existing users table
class Patients(Base):
    __table__ = db.Table('Patients', Base.metadata,
                         autoload=True, autoload_with=engine)

class Exams(Base):
    __table__ = db.Table('Exams', Base.metadata,
                         autoload=True, autoload_with=engine)

class Doctors(Base):
    __table__ = db.Table('Doctors', Base.metadata,
                         autoload=True, autoload_with=engine)

Session = db.orm.sessionmaker(engine)
session = Session()

global salt
salt = "kadsjbirebiuoyebiqelf"

# Register a doctor
@app.route('/register', methods=['POST'])
def Register():

    if (request.method == "POST"):
        print(request.method)

        user_name = request.json['username']
        password = request.json['password']
        first_name = request.json['firstname']
        last_name = request.json['lastname']

        password += salt

        Doctor_ID = session.query(Doctors).count()
 
        query = db.insert(Doctors).values(doctor_ID=Doctor_ID, username=user_name, password=hashlib.sha256(password.encode()).hexdigest(), firstname = first_name, lastname = last_name)
        conn.execute(query)

        return {0:0}

# Login to user account
@app.route('/login/<user_name>/<password>', methods=['GET'])
def Login(user_name, password):

    if (request.method == "GET"):
        print(request.method)

        HT = {}

        password += salt

        DOCTORS = metadata.tables['Doctors']
        query = db.select(DOCTORS).where(DOCTORS.c.username == user_name)
        
        result = engine.execute(query).fetchall()

        for row in result:
            if row[1] == user_name and row[2] == hashlib.sha256(password.encode()).hexdigest():
                HT[0] = 0
                return json.dumps(HT)
        
        HT[1] = 1

        return json.dumps(HT)


admin = Admin(app)
admin.add_view(ModelView(Patients, session))
admin.add_view(ModelView(Exams, session))
admin.add_view(ModelView(Doctors, session))
app.run()
