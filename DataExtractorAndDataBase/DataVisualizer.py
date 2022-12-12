import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np
import math
from math import sqrt, acos, asin, sin, atan, cos, pi
import json
import time
import random
from console_progressbar import ProgressBar

# Set the lengths of upper and lower arms
global l1
global l2
global prev_angle
global prev_time
global angles
global version
global title
global velocity

# Clear Terminal
try:
    import os
    os.system('cls')
except:
    pass

def euclidean_distance(point_1, point_2):
    
    distance = sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2 + (point_1[2] - point_2[2])**2)

    return distance

def law_cosine(a, b, c):
    # print((c**2 - a**2 - b**2)/(-2*a*b))
    return math.degrees(acos((c**2 - a**2 - b**2)/(-2*a*b)))

def angular_velocity(prev_angle, curr_angle, prev_time, curr_time, l2):
    radians = ((curr_angle - prev_angle)/180)*pi
    return abs(radians/(curr_time - prev_time)*l2)

def visualize_movement(shoulder, hand, num_entry, curr_time,  x_bound, y_bound, z_bound):

    global l1
    global l2
    global prev_angle
    global prev_time
    global velocity

    # Set the shoulder and end of arm points 
    X_data = np.array([float(shoulder[0]), float(hand[0])]) 
    Y_data = np.array([float(shoulder[1]), float(hand[1])])
    Z_data = np.array([float(shoulder[2]), float(hand[2])])

    # Calculate the euclidiean distance from the shoulder, (x1, y1, z1), to the hand, (x2, y2, z2)
    norm_v = sqrt((X_data[1] - X_data[0])**2 + (Y_data[1] - Y_data[0])**2 + (Z_data[1] - Z_data[0])**2) 

    # Check system feasibilty

    # print(f"Distance: {norm_v} Shoulder: {shoulder} Hand: {hand}\n")

    if(norm_v > l1 + l2):
        raise Exception("System not possible (out of max reach); Suggested to increase l1, l2 or choose new points\n")

    # Solve for theta 1 using law of cosines
    theta_1 = law_cosine(l1, norm_v, l2)

    # Solve for theta 2 using law of cosines
    theta_2 = law_cosine(l2, norm_v, l1)

    # Solve for theta 3 given theta 1 and 2
    theta_3 = 180 - (theta_1 + theta_2)

    # print(theta_1, theta_2, theta_3)

    
    if num_entry != 0:
        # print(f"Angular velocity: {angular_velocity(prev_angle, theta_3, prev_time, curr_time, l2)}")

        velocity.append(angular_velocity(prev_angle, theta_3, prev_time, curr_time, l2))

        prev_angle = theta_3
        prev_time = curr_time
    else:
        prev_angle = theta_3
        prev_time = curr_time

    #####################################################################################
    
    # 2D PLOT

    # Plot the Shoulder and End of Arm Points

    # azimuths = np.radians(np.linspace(0, theta_3, 20))
    # zeniths = np.arange(0, 70, 10)

    # r, theta = np.meshgrid(zeniths, azimuths)
    # values = np.random.random((azimuths.size, zeniths.size))

    # #-- Plot... ------------------------------------------------
    # # fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    # ax.contourf(theta, r, values)
    # ax.set_theta_zero_location("N")

    # plt.show()

    #####################################################################################

    # # 3D PLOT

    # # Plot the Shoulder and End of Arm Points
    # ax.scatter3D(X_data, Y_data, Z_data, c=Z_data, cmap='Spectral')

    # # Plot a line from the shoulder to the end of arm
    # # ax.plot([X_data[0], X_data[1]], [Y_data[0], Y_data[1]], [Z_data[0], Z_data[1]])

    # # Solve for the endpoints of l1 (shoulder to elbow)
    # m = (Y_data[1] - Y_data[0])/(X_data[1] - X_data[0])
    # a = 1 + m**2
    # b = -2*X_data[0] - 2*(m**2)*X_data[0]
    # c = X_data[0]**2 + (m**2)*(X_data[0]**2) - l1**2

    # X_Sol = [(-b + sqrt(b**2 - 4*a*c))/(2*a), (-b - sqrt(b**2 - 4*a*c))/(2*a)]
    # Y_Sol = [m*(X_Sol[0] - X_data[0]) + Y_data[0], m*(X_Sol[1] - X_data[0]) + Y_data[0]]

    # # Choose the point closest to the end of arm
    # best_point = []
    # distance = l1 + l2

    # for i in range(2):
    #     if(sqrt((X_data[1] - X_Sol[i])**2 + (Y_data[1] - Y_Sol[i])**2) < distance):
    #         best_point = [X_Sol[i], Y_Sol[i], Z_data[0]]
    #         distance = sqrt((X_data[1] - X_Sol[i])**2 + (Y_data[1] - Y_Sol[i])**2)
    
    # # ax.set_xlim(x_bound)
    # # ax.set_ylim(y_bound)
    # # ax.set_zlim(z_bound)

    # # Plot the upper and lower arms
    # ax.plot([X_data[0], best_point[0]], [Y_data[0], best_point[1]], [Z_data[0], Z_data[0]])
    # ax.plot([X_data[1], best_point[0]], [Y_data[1], best_point[1]], [Z_data[1], Z_data[0]])

    # # Label the shoulder, elbow, and end of hand
    # ax.text(X_data[0], Y_data[0], Z_data[0],  f"Shoulder {round(theta_1, 3)}", color='k')
    # ax.text(best_point[0], best_point[1], best_point[2],  f"Elbow {round(theta_3, 3)}", color='k')
    # ax.text(X_data[1], Y_data[1], Z_data[1],  f"End of Arm {round(theta_2, 3)}", color='k')

    # plt.show()

    return theta_3

def get_time():

    global version

    pb = ProgressBar(total=len(angles), suffix='Completed', decimals=3, length=50, fill='X', zfill='-')
    
    while True: 
        try:   
            version += 1

            pb.print_progress_bar(version)

            yield times[version]

        except:
            break

def update(_time):

    global angles
    global version
    global title

    i = version

    
    if len(angles) <= i:
        return title,

    theta_3 = angles[i]

    ax.cla()

    # 2D PLOT

    # Plot the Shoulder and End of Arm Points

    azimuths = np.radians(np.linspace(0, theta_3, 20))
    zeniths = np.arange(0, 2, 1)

    r, theta = np.meshgrid(zeniths, azimuths)
    values = np.random.random((azimuths.size, zeniths.size))

    #-- Plot... ------------------------------------------------
    # fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ax.contourf(theta, r, values)
    ax.set_theta_zero_location("N")

    title = ax.text(0.8,1, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},transform=ax.transAxes, ha="left")
    title.set_text(u"Angle: {}°\nTime: {}\nStep: {}/{}".format(round(theta_3, 3), round(_time, 3), i, len(angles)))

    # time.sleep(0.5)
    #plt.pause(0.5)

    plt.draw()
    return title,
    

##########################################################################################################################

# Get Hand's Positional Data

# Position of the 3 joints
arm_points_path = r"C:/Users/siddi/AppData/LocalLow/DefaultCompany/CSE-120-Fall-120-VCH/PositionData.json"

points = []

with open(arm_points_path, 'r') as f:

    arr = []

    for i, row in enumerate(f):
        my_dict = json.dumps(row)

        if("x" in my_dict or "y" in my_dict or "z" in my_dict):
            
            position = ""

            for char in my_dict:
                try:
                    if char == ".":
                        position += char
                        continue

                    temp = str(int(char))
                    position += temp
                except:
                    pass
            
            if len(arr) < 3:
                arr.append(float(position))
            else:
                points.append(arr)
                arr = []
                arr.append(float(position))

    points.append(arr)

fit = 0
works = False

while works == False:

    # Calculate the distance of the upper and lower arms

    l1 = euclidean_distance(points[0], points[1]) + fit
    l2 = euclidean_distance(points[1], points[2]) + fit

    # Object's Positional Data
    object_position_path = r"C:/Users/siddi/AppData/LocalLow/DefaultCompany/CSE-120-Fall-120-VCH/ObjectPositionData.json"

    df = pd.DataFrame(columns=['x','y','z', 'time'])

    # fig = plt.figure()
    # ax = plt.axes(projection='3d')

    # fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))

    # Set the shoulder's position
    shoulder = points[0]

    # Get the position of the hand and corresponding times
    hand_positions = []
    times = []

    with open(object_position_path, 'r') as f:

        arr = []

        for i, row in enumerate(f):
            my_dict = json.dumps(row)

            # print(my_dict)

            if("x" in my_dict or "y" in my_dict or "z" in my_dict):
                
                position = ""

                for char in my_dict:
                    try:
                        if char == ".":
                            position += char
                            continue

                        temp = str(int(char))
                        position += temp
                    except:
                        pass
                
                if len(arr) < 3:
                    arr.append(float(position))
                else:
                    hand_positions.append(arr)
                    arr = []
                    arr.append(float(position))

            elif "Time" in my_dict:

                position = ""

                for char in my_dict:
                    try:
                        if char == ".":
                            position += char
                            continue

                        temp = str(int(char))
                        position += temp
                    except:
                        pass

                times.append(float(position))

        hand_positions.append(arr)

    # print(hand_positions)

    # Get the min-max of each dimension (x, y, z)

    x_min = 2147483647
    x_max = -2147483647
    y_min = 2147483647
    y_max = -2147483647
    z_min = 2147483647
    z_max = -2147483647

    for row in hand_positions:

        if row[0] < x_min:
            x_min = row[0]

        if row[0] > x_max:
            x_max = row[0]

        if row[1] < y_min:
            y_min = row[1]

        if row[1] > y_max:
            y_max = row[1]

        if row[2] < z_min:
            z_min = row[2]

        if row[2] > z_max:
            z_max = row[2]


    x_bound = [x_min - 0.1, x_max + 0.1]
    y_bound = [y_min - 0.1, y_max + 0.1]
    z_bound = [z_min - 0.1, z_max + 0.1]

    # print(x_bound, y_bound, z_bound)
    # time.sleep(2)

    angles = []
    velocity = []

    try:
        for i, row in enumerate(hand_positions):
            # Set the postion of the hand
            hand = row
            
            angles.append(visualize_movement(shoulder, hand, i, times[i], z_bound, y_bound, x_bound))
            
            # plt.draw()
            # plt.pause(0.1)
            # ax.cla()

        works = True

    except:

        fit += 0.00001
        works = False

print(f"fit = {fit}")

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))

version = 0

anim = FuncAnimation(fig, update, get_time, interval=100, blit=True, repeat=False, save_count=len(times))

# anim = FuncAnimation(fig, update, frames = len(angles), interval=100)
anim.save('AngleAnim.gif') 

# Extract the maximum (closest to self) angle and the time spent within +/- x degrees of it

max_angle = min(angles)
index = angles.index(max_angle)

# Specify +/- x degrees
tolerance = 5

# Find the longest time interval the patient was able to hold their hand nearest to themselves
max_interval = 0
max_start = 0
max_end = 0

curr_max = 0
curr_start = 0
curr_end = 0

for i, entry in enumerate([angle - max_angle for angle in angles]):

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

print(f"Spent {round(times[max_end] - times[max_start], 5)} seconds within {tolerance} degrees of the max angle of {round(max_angle, 5)}")