# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import json
import sqlite3
from datetime import datetime

from sqlalchemy import null

#from flask_restful import Api, Resource
app = Flask(__name__, static_url_path='', static_folder='')


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///VCH_VR_DB.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
#db.create_all()

class Patient(db.Model):
   __tablename__ = 'patient'
   id = db.Column(db.String(25), primary_key = True)
   first_name = db.Column(db.String(25))
   last_name = db.Column(db.String(25))
   
   def __init__(self, id, fname, lname):
      self.id = id
      self.first_name = fname
      self.last_name = lname
   def __repr__(self):
      return "<Patient id %r, Name: %r %r" % (self.id, self.first_name, self.last_name)

class Exams(db.Model):
   __tablename__ = 'exam'
   id = db.Column(db.String(25), primary_key = True)
   pat_ID = db.Column(db.String(25))
   exam_date = db.Column(db.String(20))
   curl_test_angle_result = db.Column(db.Float(10))
   curl_test_velocity_result = db.Column(db.Float(10))
   curl_test_strength_result = db.Column(db.Float(10))
   draw_shape_time_result = db.Column(db.Float(10))
   
   def __init__(self, id, pat_id,date,cta_res, ctv_res, cts_res, draw):
      self.id = id
      self.pat_ID = pat_id
      self.exam_date = date
      self.curl_test_angle_result = cta_res
      self.curl_test_velocity_result = ctv_res
      self.curl_test_strength_result = cts_res
      self.draw_shape_time_result = draw
   def __repr__(self):
      return "<Exam id: %r, Exam Date: %r, Patiend id: %r >" % (self.id, self.exam_date, self.pat_ID)



# Main landing page with 2 options
@app.route('/')
def start():
   #render the html template
   return render_template("main_landing.html") #jsonify(grades_dict)

# Enter Patient ID Page
@app.route('/patient_selection')
def patient_selection():
   return render_template('patient_selection.html')

# Report Selection HTML Page
@app.route('/rep_sel')
def rep_select():
   return render_template('report_selection.html')

# # Show all exams of single patient
# @app.route('<int:patID>/rep_sel/exams', methods=['GET'])
# def exams(patID):
#    exms = Exams.query.all(Exams.pat_ID==patID)
#    return render_template('exam_selection.html', exams=exms)




### Old route links for db interaction
@app.route('/<string:name>', methods=['POST'])
def new_pat(name):
   # create new patient 
   split_name = name.split(' ')
   new_patient = Patient(first_name=split_name[0], last_name=split_name[1])
   # Add the new patient to the database
   db.session.add(new_patient)
   db.session.commit()
   #return render_template('')
   return "Patient %s %s has been created. \n Patient ID: %s".format(split_name[0], split_name[1], "1111")

@app.route('/<string:patient>/exams', methods=['POST'])
def new_exam(patient):
   split_name = patient.split(' ')
   # create new exam -- holds the results of analyzed exam 
   new_exam = Exams()
   # Add the new exam to the exams database, will need the patient ID for verification
   db.session.add(new_exam)
   db.session.commit()
   return "Patient %s %s taken Exam %s on %s.".format(split_name[0], split_name[1], "1234", "11/1/2022")

@app.route('/<string:patient>/exams', methods = ['POST' ,'GET'])
def exams(patient):
## GET ALL EXAMS METHOD ##   
   if request.method == 'GET':
      #create a temp dictionary to return for the js to parse through and print
      exams_dict = {}
      rows = Exams.query.all()
      for row in rows:
         exams_dict[row.patient_ID] = row.patient_ID + " " + row.exam_date

      # return the entire dictionary for the js file to parse through
      return exams_dict


# @app.route('/init_exam', methods=['GET'])
# def init_exam(patID):
#    # 
#    # UNITY 


@app.route('/<string:patient_ID>/<string:exam_ID>', methods=['GET','DELETE'])
def pat_exams(patient_ID, exam_ID=None):

## GET SINGLE EXAM METHOD ##
   if request.method == 'GET':
      # return the exam of the patient
      patient_exam = Exams.query.filter_by(id=exam_ID)
      #check if the exam exist in the database
      if(patient_exam is None):
         return "Cannot Find Exam %s for Patient %s %s".format(exam_ID, first_name, last_name)
     #return patient exam
      return patient_exam

## DELETE SINGLE EXAM METHOD ##
   if request.method == 'DELETE':
      deleted_exam = Exams.query.filter_by(id = exam_ID).first()
      db.session.delete(deleted_exam)
      db.session.commit()
      
      #return message upon successful deletion of exam
      return "Exam %s, has been deleted from Patient %s %s".format(exam_ID, first_name, last_name)
   


## run the app
if __name__ == '__main__':
   #db.create_all()
   app.run(debug= True) # do not have to rerun the program, will refresh with debug


