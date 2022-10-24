import sqlite3
import datetime
import random

# Connect to DB
try:
    conn = sqlite3.connect("VCH_VR_DB.db")
    print("Connected to DB\n")
except:
    pass

# Drop Tables
try:
    sql='''DROP TABLE Patient;'''
    conn.execute(sql)

    sql='''DROP TABLE Exams;'''
    conn.execute(sql)
except:
    pass

'''
entries for exams table
max angle of elbow
velocity
time diff of each task
date of exam
potential diagnosis for each task
'''
# Create Tables
try:
    sql = '''CREATE TABLE Patient (
        patient_ID VARCHAR(25) PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL
    );'''

    conn.execute(sql)

    sql = '''CREATE TABLE Exams (
        exam_ID VARCHAR(25) PRIMARY KEY,
        patient_ID VARCHAR(25) NOT NULL,
        exam_date timestamp,
        curl_test_angle_result DOUBLE,
        curl_test_velocity_result DOUBLE,
        curl_test_strength_result DOUBLE,
        draw_shape_time_result timestamp
    );'''

    conn.execute(sql)
except:
    pass

sql = '''INSERT INTO Patient (patient_ID, first_name, last_name)
VALUES(?,?,?);'''
cur = conn.cursor()

first_names = ["abby", "bob","charles","daryl", "eugene", "fred", "george", "harvey", "ingrid","jaucque","keith","liam","mason","nigel","oswald","pierre","quinton", "ronald", 'seth', "tabitha", "uiqua", "vector", "william", "xavier","yolaina","zach"]
last_names = ["zinc","schmidt","barkley","oate","porter","wealsey","lopez","dent","ingrown","parlay","hamburger","neeson","mount","guido", "cobblepot", "white","tarentino","mcdonald","rogan", "galavan", "normal","addition","shakespeare","wolff","jeager","andcody"]

for i in range(26):
    cur.execute(sql, (i, first_names[i], last_names[i]))

conn.commit()

sql = '''INSERT INTO Exams (exam_ID, patient_ID, exam_date, curl_test_angle_result, curl_test_velocity_result,curl_test_strength_result,draw_shape_time_result)
VALUES(?,?,?,?,?,?,?);'''
cur = conn.cursor()

for i in range(100):
    cur.execute(sql, (i, random.randint(0, 25), datetime.datetime.now(),random.randint(0, 180),random.randint(0, 180),random.randint(0, 180),datetime.datetime.now()))

conn.commit()

patient_ID = input("Enter a patient ID: ")

sql = f'''SELECT *
FROM Exams, Patient
WHERE (Patient.patient_ID = Exams.patient_ID) AND
    (Patient.patient_ID = {patient_ID});'''

cur.execute(sql)

rows = cur.fetchall()

for row in rows:
    print(row)


'''
For all exams of a single patient:
    SELECT *
    FROM Exams, Patient
    WHERE (Patient.patient_ID = Exams.patient_ID) AND
    (Patient.first_name = 'oswald');


'''

patient_ID = input("Enter conditions to filter data by: ")

sql = f'''SELECT *
FROM Exams, Patient
WHERE (Patient.patient_ID = Exams.patient_ID) AND
    (Patient.patient_ID = {patient_ID});'''

cur.execute(sql)

rows = cur.fetchall()

for row in rows:
    print(row)

