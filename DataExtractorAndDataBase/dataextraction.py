import metric_utils as mu
import util

import sqlalchemy as db
import sqlalchemy
from sqlalchemy.ext.automap import automap_base

from datetime import date
import sys


# TODO: DEBUG INSERT INTO DATABASE FUNCTION
def insertintoDB():
    # Connect to the database
    engine = db.create_engine('sqlite:///VRDataBase.sqlite?check_same_thread=False')
    conn = engine.connect()
    metadata = db.MetaData()

    Base = automap_base()
    Base.prepare(engine, reflect=True)

    Exams = Base.classes.Exams

    # query = db.insert(Exams).values(exam_ID = )
    # conn.execute(query)


def getMetrics(patient_measurements, positional_data):

    l1, l2 = mu.armLength(patient_measurements)
    angleList = mu.flexionAngleList(l1, l2, patient_measurements)

    angle = mu.angleMetric(angleList)
    velocity = mu.instVelocityList(angleList, positional_data)
    time = mu.timeMetric(angleList, positional_data, angle)

    strengthclass = mu.strengthClassMetric(angle, time)

    return angle, velocity, strengthclass


def main(patient_id):
    # # TODO: REPLACE JSON FILEPATH ACCORDINGLY
    patient_measurements_path = r"/Users/shreyashriram/Documents/120/CSE-120-Fall-2022---VCH/Angle and Angular Velocity/PositionData.json"
    position_data_path = r"/Users/shreyashriram/Documents/120/CSE-120-Fall-2022---VCH/Angle and Angular Velocity/ObjectPositionData.json"

    patient_measurements = util.parseJSON(patient_measurements_path)
    position_data = util.parseJSON(position_data_path)

    exam_date = date.today()
    angle, velocity, strengthclass = getMetrics(patient_measurements, position_data)


if __name__ == "__main__":
    patient_id = sys.argv[1]
    main(patient_id)