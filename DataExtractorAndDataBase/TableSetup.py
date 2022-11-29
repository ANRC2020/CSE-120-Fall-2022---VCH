import sqlalchemy as db
from sqlalchemy import select, Table

try:
    import os
    os.system('cls')
except:
    pass

# Routine for dropping all tables

def Drop_Table(table):

    sql = f'DROP TABLE IF EXISTS {table};'
    engine.execute(sql)

# Routines for defining each table

def Initialize_Doctors():

    # Define and Create the Doctors Table
    Doctors = db.Table('Doctors', metadata,
        db.Column('doctors_ID', db.Integer(), primary_key=True, nullable=False),
        db.Column('username', db.String(255), nullable=False),
        db.Column('password', db.String(255), nullable=False),
        db.Column('firstname', db.String(255), nullable=False),
        db.Column('lastname', db.String(255), nullable=False)
    )

    metadata.create_all(engine)  # Creates the table

def Initialize_Patients():

    # Define and Create the Patients Table
    Patients = db.Table('Patients', metadata,
        db.Column('patient_ID', db.Integer(), primary_key=True, nullable=False),
        db.Column('firstname', db.String(255), nullable=False),
        db.Column('lastname', db.String(255), nullable=False)
    )

    metadata.create_all(engine)  # Creates the table

def Initialize_Exams():

    # Define And Create The Exams Table
    Exams = db.Table('Exams', metadata,
        db.Column('exam_ID', db.Integer(), primary_key=True, nullable=False),
        db.Column('patient_ID', db.Integer(), nullable=False),
        db.Column('exam_date', db.String(50), nullable=False),
        db.Column('max_angle', db.Float(), nullable=False),
        db.Column('max_velocity', db.Float(), nullable=False),
        db.Column('strength_class', db.Integer(), nullable=False),
        db.Column('tasks', db.String(255), nullable=False),
        db.Column('percent_tasks_completed', db.Float(), nullable=False)
    )

    metadata.create_all(engine)  # Creates the table

# Connect to the database
engine = db.create_engine('sqlite:///VRDataBase.sqlite?check_same_thread=False')
conn = engine.connect()
metadata = db.MetaData()


# Reset the database

def Reset_Database():

    # Load Patients
    try:
        patients = Table('Patients', metadata, autoload=True, autoload_with=engine)
    except:
        Drop_Table('Patients')
        patients = Initialize_Patients()

    # Load Exams
    try:
        exams = Table('Exams', metadata, autoload=True, autoload_with=engine)
    except:
        Drop_Table('Exams')
        exams = Initialize_Exams()

    # Load Doctors
    try:
        doctors = Table('Doctors', metadata, autoload=True, autoload_with=engine)
    except:
        Drop_Table('Doctors')
        doctors = Initialize_Doctors()

    print("Database Ready!\n")

    return patients, exams, doctors