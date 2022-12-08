from sqlalchemy.ext.declarative import declarative_base
import json
from flask import Flask, request, jsonify, render_template,  redirect, url_for
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
import subprocess

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

# convert a sql alchemy row to dictionary
def convert_dict(result):
    metric_list = []
    for row in result:
        metric_list.append(row)
    return metric_list

#### API BEGINS -------------------

## This method is the landing page that the site will open up to
# Has two options for the client to choose
@app.route('/')
def start():
   #render the main landing  template
   return render_template("home.html")


## This method will return all fo the exams of a single patient
## Pass through the patient id for all fo the exams query
@app.route('/report/<p_id>/exams', methods=['GET'])
def exams_list(p_id):
    if request.method == 'GET':
        query = exams.select().where(exams.c.patient_ID==p_id)
        result = conn.execute(query)
        Exams = []
        for exam in result:
            Exams.append(convert_dict(exam))
        print(Exams)
        return json.dumps(Exams)
        #result = json.dumps([exam for exam in result])
        #jsonify({'result': [dict(exam) for exam in result]})
        return render_template('report_part1.html', exams=result)


## This method will return a single exam contents
## Pass thorugh the patient id and the exam id for the query
@app.route('/report/<p_id>/<exid>', methods=['GET', 'POST'])
def get_exam_report(p_id, exid):
    if request.method == 'POST':
        query = exams.select().where(exams.c.exam_ID==exid and exams.c.patient_ID==p_id)
        result = conn.execute(query)
        Exam = convert_dict(result)
        print(Exam)
        # return Exam
        return render_template('report_final.html', exam=Exam)

'''
    ---------- Start the Unity VR UI ----------
'''
@app.route('/exam_start/<p_id>', methods=['POST'])
def exam_start(p_id):
    #p_id = request.form.get('patient_id')
    # print("patient id = ", p_id)
    # query = exams.select(firstname, lastname).where(exams.c.patient_ID==p_id)
    # result = conn.execute(query)

    # result = [exam for exam in result]
    # print(result)
    # exam = session.query(Exams.patient_ID==p_id)
    # return result

    ## ENTER SHREYA's CODE
    # This launches a Unity exe application from command prompt with no additional string arguments
    # Verified on Chloe's windows - works on Command prompt and powershell, not ubuntu
    subprocess.Popen(r"C:\Users\chloe\Desktop\VCH_Project\VR_Exam\UnityGame\CSE-120-Fall-120-VCH.exe", shell=True)
    
    # Return to the home page for report access
    return render_template('report_final.html')

### ----- Navigation for pages -----
@app.route('/report', methods=['GET'])
def report1():
    # exams = exams_list()
    # print(exams)
    return render_template('report_part1.html')#, exams=exams)

@app.route('/report2', methods=['GET'])
def report2():
    # exams = exam()
    # print(exams)
    return render_template('report_final.html')#, exam=exam)

@app.route('/exam', methods=['GET'])
def exam1():
    return render_template('exam_part1.html')








##### ------ LOGIN/REGISTER BEGINS
# Register a doctor
@app.route('/register', methods=['POST','GET'])
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

        return render_template('register.html')
    return render_template('register.html')
    # else:
    #     if current_user.is_authenicated:
    #         return render_template('main_landing.html')
    #     return render_template('register.html')

# Login to user account <user_name>/<password>
@app.route('/login', methods=['GET'])
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
        #return render_template('home.html')
    return render_template('login.html')

@app.route('/login', methods=['GET'])
def Logout(user_name, password):
	logout_user()
	flash('Logged out.')
	return redirect(url_for('Login'))

admin = Admin(app)
admin.add_view(ModelView(Patients, session))
admin.add_view(ModelView(Exams, session))
admin.add_view(ModelView(Doctors, session))


app.run(debug= True)