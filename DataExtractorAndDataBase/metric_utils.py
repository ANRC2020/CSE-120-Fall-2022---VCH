import util 

def armLength(patient_measurements):
    # This function returns the calculated forearm and arm measurements of the patient based on the three tagged positions. 
    # Input: 
    #   patient_measurements (dict): containing shoulder, elbow, palm (x, y, z) information 
    # Output: 
    #   forearm, arm (int) measurements based on euclidian distance

    forearm = util.euclidean_distance(patient_measurements[0], patient_measurements[1])
    upperarm = util.euclidean_distance(patient_measurements[1], patient_measurements[2])
    
    return forearm, upperarm


def angleAndVelocityList(forearm, upperarm, positional_data, shoulder_loc, timestamps):
    # This function returns a list of angles for each time step in the positional_data list
    # Input: 
    #   forearm (int)
    #   upperarm (int)
    #   positional_data (dict): containing list (length = n) of positional data (x, y, z)
    #   shoulder_loc (float list, [x, y, z])
    #   timestamps (list)
    # 
    # Output: 
    #   angleList (list): angles between each time step in the positional_data list
    #   velocityList (list)): velocity between each time step in the positional_data list
    
    max_distance = forearm + upperarm
    angleList = []
    instVelocityList = []
    
    prev_angle = 0
    curr_angle = 0
    prev_time = timestamps[0]
    curr_time = timestamps[0]

    for i in (positional_data):

        norm_v = util.euclidean_distance(positional_data[i], shoulder_loc)
        
        if(norm_v > max_distance):
            raise Exception("System not possible (out of max reach); Suggested to increase l1, l2 or choose new points\n")

        # Solve for theta 1 using law of cosines
        theta_1 = util.law_cosine(upperarm, norm_v, forearm)

        # Solve for theta 2 using law of cosines
        theta_2 = util.law_cosine(forearm, norm_v, upperarm)

        # Solve for theta 3 given theta 1 and 2
        angle = 180 - (theta_1 + theta_2)

        angleList.append(angle)

        curr_time = timestamps[i]

        if i != 0:
            instVelocityList.append(util.velocity(prev_angle, angle, prev_time, curr_time, forearm))
            prev_angle = angleList[i-1]
            prev_time = curr_time
        
        else:
            prev_angle = angle
            prev_time = curr_time

    return  angleList, instVelocityList

################################ METRIC EXTRACTION ################################

def angleMetric(angleList):
    # This function returns the minimum angle (between forearm and arm) the patient was able to make during the exam
    # Input: 
    #   angleList (list): angles for each time step in the positional_data list 
    # Output: 
    #   angleMetric (int): minimum angle
  
    angleMetric = min(angleList)
    return angleMetric

def timeMetric(angleList, timestamps, angleMetric):
    # Function returns the amount of time a patient maintained the smallest angle flexion by finding the longest subset of the anglelist
    # Input: 
    #   angleList (list): angles for each time step in the positional_data list 
    #   positional_data (dict): containing list (length = n) of positional data (x, y, z, t)
    #   angleMetric (int): minimum angle

    # Output: 
    #   t (int): how long the minimum angle was maintained
    
    # Specify +/- x degrees
    tolerance = 5
    index = angleList.index(angleMetric)

    # Find the longest time interval the patient was able to hold their hand nearest to themselves
    max_interval = 0
    max_start = 0
    max_end = 0

    curr_max = 0
    curr_start = 0
    curr_end = 0

    for i, entry in enumerate([angle - angleMetric for angle in angleList]):
        if entry <= tolerance:
            curr_max += 1

            if curr_max == 1:
                curr_start = i
                curr_end = i
            
            else:
                curr_end = i
        
        else:

            if curr_max > max_interval:
                max_interval = curr_max
                max_start = curr_start
                max_end = curr_end

            curr_max = 0
            curr_start = 0
            curr_end = 0

    t = timestamps[max_end] - timestamps[max_start]
    return t

def velocityMetric(velocityList):
    # This function returns the maximum velocity the patient was able to achieve during the exam
    # Input: 
    #   velocityList (list, length = n-1): velocity for each time step in the positional_data list
    # Output: 
    #   velocityMetric (int) : maximum velocity
   
    velocityMetric = max(velocityList) 
    return velocityMetric

def strengthClassMetric(angleMetric, timeMetric, velocityMetric):
    # This function returns the strength class metric [0, 5] based on the measured angle and time metric and classification scheme
    # Input:
    #   angleMetric (int): minimum angle
    #   timemetric (int): maximum velocity
    #   velocityMetric (int) : maximum velocity
    # Output: 
    #   strengthClass (int): 

    healthy_buffer = 45
    significant_angle = 120

    
    strengthClass = 0

    # Is there movement?
    if (velocityMetric > 0): 
        strengthClass = 1
    
        if (angleMetric > significant_angle):
            strengthClass = 2
        
        # Patient made it passed significant angle range
        else: 
            strengthClass = 3

            # Did the patient hold up their hand at a significant angle?
            if (timeMetric >= 5 ): 
                strengthClass = 4

                # Patient achieved small angle and time 
                if (angleMetric <= healthy_buffer):
                    strengthClass = 5

    return strengthClass

# TODO: UPDATE VISUALIZATION PATH
def dataVisualization(angleList):
    # This function produces a gif animation of the angles made during the exam
    print('this is the visualization of the past exam')