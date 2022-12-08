def armLength(patient_measurements):
    # This function returns the calculated forearm and arm measurements of the patient based on the three tagged positions. 
    # Input: 
    #   patient_measurements (dict): containing shoulder, elbow, palm (x, y, z) information 
    # Output: 
    #   forearm, arm (int) measurements based on euclidian distance

    forearm = 0
    arm = 0
    
    return forearm, arm


def flexionAngleList(forearm, arm, positional_data):
    # This function returns a list of angles for each time step in the positional_data list
    # Input: 
    #   forearm (int)
    #   arm (int)
    #   positional_data (dict): containing list (length = n) of positional data (x, y, z, t)

    # Output: 
    #   angleList (list, length = n-1): angles for each time step in the positional_data list
    
    angleList = []
    return  angleList

def instVelocityList(angleList, positional_data):
    # This function returns calculated list of instantanious velcity for each time step in the positional_data list
    # Input: 
    #   angleList (list, length = n-1): angles for each time step in the positional_data list
    #   positional_data (dict): containing list (length = n) of positional data (x, y, z, t)

    # Output: 
    #   velocityList (list, length = n-1): velocity for each time step in the positional_data list
    
    velocityList = []
    return  velocityList


################################ METRIC EXTRACTION ################################

def angleMetric(angleList):
    # This function returns the minimum angle (between forearm and arm) the patient was able to make during the exam
    # Input: 
    #   angleList (list): angles for each time step in the positional_data list 
    # Output: 
    #   angleMetric (int): minimum angle
  
    angleMetric = min(angleList)
    return angleMetric

def timeMetric(angleList, positional_data, angleMetric):
    # Function returns the amount of time a patient maintained the smallest angle flexion by finding the longest subset of the anglelist
    # Input: 
    #   angleList (list): angles for each time step in the positional_data list 
    #   positional_data (dict): containing list (length = n) of positional data (x, y, z, t)
    #   angleMetric (int): minimum angle

    # Output: 
    #   t (int): how long the minimum angle was maintained

    t = 0
    return t

def velocityMetric(velocityList):
    # This function returns the maximum velocity the patient was able to achieve during the exam
    # Input: 
    #   velocityList (list, length = n-1): velocity for each time step in the positional_data list
    # Output: 
    #   velocityMetric (int) : maximum velocity
   
    velocityMetric = max(velocityList) 
    return velocityMetric

def strengthClassMetric(angleMetric, time):
    # This function returns the strength class metric [0, 5] based on the measured angle and time metric and classification scheme
    # Input:
    #   angleMetric (int): minimum angle
    #   timemetric (int): maximum velocity
    # Output: 
    #   strengthClass (int): 

    healthy_buffer = 45
    significant_angle = 120
    sensing = True
    
    strengthClass = 0
    return strengthClass


def dataVisualization(angleList):
    # This function produces a gif animation of the angles made during the exam.
