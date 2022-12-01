# TODO: switch to config file
# config variables
healthy_buffer = 45
significant_angle = 110
sensing = True

def getPatientId():
    return 1

def getAngle():
    return 0

def getVelocity():
    return 0

def getTime(position_array, velocity_array):
    s = 0
    return s

def getStrengthClass(theta):

    s = getTime()
    rating = 0
    
    if (sensing):
        rating = 2
    
    if (theta > significant_angle):
        rating = rating+1

    if (s >= 3):
        rating = rating+1
    
    
    return 0


