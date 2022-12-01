from datetime import date
import metric_utils

def exam_info():
    exam_date = date.today()
    patient_id = metric_utils.getPatientId()
    task = 'A'
    percentage_tasks_completed = 1

    return exam_date, patient_id, task, percentage_tasks_completed

def exam_metrics():
    angle_flexion = metric_utils.getAngle()
    velocity_flexion = metric_utils.getVelocity()
    strength_class = metric_utils.getStrengthClass()

    return angle_flexion, velocity_flexion, strength_class

def main():
    # GET .TXT FILE
    # import arm_measurements txt file
        # patient_name
        # shoulder (x, y, z)
        # elbow (x, y, z)
        # palm (x, y, z)

    # import  positional/velocity txt file
        # velcities = [(x, y, z), (x, y, z), (x, y, z)]
        # positions = [(x, y, z), (x, y, z), (x, y, z)]

    a, b, c, d  = exam_info()
    e, f, g = exam_metrics()

    # insert a-g into database
    

    # return exam_id
    

if __name__ == "__main__":
    main()