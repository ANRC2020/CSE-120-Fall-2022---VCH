import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from math import sqrt, acos, asin, sin, atan, cos

# Set the lengths of upper and lower arms
global l1
global l2
global prev_angle

def law_cosine(a, b, c):
    print((c**2 - a**2 - b**2)/(-2*a*b))
    return math.degrees(acos((c**2 - a**2 - b**2)/(-2*a*b)))

def angular_velocity(prev_angle, curr_angle, delta_t):
    return abs((curr_angle - prev_angle)/delta_t)

def visualize_movement(shoulder, hand, num_entry):

    global l1
    global l2
    global prev_angle

    # Set the shoulder and end of arm points 
    X_data = np.array([float(shoulder[0]), float(hand[0])]) 
    Y_data = np.array([float(shoulder[1]), float(hand[1])])
    Z_data = np.array([float(shoulder[2]), float(hand[2])])

    # Calculate the euclidiean distance from the shoulder, (x1, y1, z1), to the hand, (x2, y2, z2)
    norm_v = sqrt((X_data[1] - X_data[0])**2 + (Y_data[1] - Y_data[0])**2 + (Z_data[1] - Z_data[0])**2)

    # Check system feasibilty
    if(norm_v > l1 + l2):
        raise Exception("System not possible (out of max reach); Suggested to increase l1, l2 or choose new points\n")

    # Solve for theta 1 using law of cosines
    theta_1 = law_cosine(l1, norm_v, l2)

    # Solve for theta 2 using law of cosines
    theta_2 = law_cosine(l2, norm_v, l1)

    # Solve for theta 3 given theta 1 and 2
    theta_3 = 180 - (theta_1 + theta_2)

    print(theta_1, theta_2, theta_3)

    
    if num_entry != 0:
        print(f"Angular velocity: {angular_velocity(prev_angle, theta_3, 0.1)}")
        prev_angle = theta_3
    else:
        prev_angle = theta_3

    # Plot the Shoulder and End of Arm Points
    ax.scatter3D(X_data, Y_data, Z_data, c=Z_data, cmap='Spectral')

    # Plot a line from the shoulder to the end of arm
    # ax.plot([X_data[0], X_data[1]], [Y_data[0], Y_data[1]], [Z_data[0], Z_data[1]])

    # Solve for the endpoints of l1 (shoulder to elbow)
    m = (Y_data[1] - Y_data[0])/(X_data[1] - X_data[0])
    a = 1 + m**2
    b = -2*X_data[0] - 2*(m**2)*X_data[0]
    c = X_data[0]**2 + (m**2)*(X_data[0]**2) - l1**2

    X_Sol = [(-b + sqrt(b**2 - 4*a*c))/(2*a), (-b - sqrt(b**2 - 4*a*c))/(2*a)]
    Y_Sol = [m*(X_Sol[0] - X_data[0]) + Y_data[0], m*(X_Sol[1] - X_data[0]) + Y_data[0]]

    # Choose the point closest to the end of arm
    best_point = []
    distance = l1 + l2

    for i in range(2):
        if(sqrt((X_data[1] - X_Sol[i])**2 + (Y_data[1] - Y_Sol[i])**2) < distance):
            best_point = [X_Sol[i], Y_Sol[i], Z_data[0]]
            distance = sqrt((X_data[1] - X_Sol[i])**2 + (Y_data[1] - Y_Sol[i])**2)

    # Plot the upper and lower arms
    ax.plot([X_data[0], best_point[0]], [Y_data[0], best_point[1]], [Z_data[0], Z_data[0]])
    ax.plot([X_data[1], best_point[0]], [Y_data[1], best_point[1]], [Z_data[1], Z_data[0]])

    # Label the shoulder, elbow, and end of hand
    # ax.text(X_data[0], Y_data[0], Z_data[0],  f"Shoulder {round(theta_1, 3)}", color='k')
    ax.text(best_point[0], best_point[1], best_point[2],  f"Elbow {round(theta_3, 3)}", color='k')
    # ax.text(X_data[1], Y_data[1], Z_data[1],  f"End of Arm {round(theta_2, 3)}", color='k')

    # plt.show()

##########################################################################################################################

# Get Hand's Positional Data
path = r"C:\Users\siddi\OneDrive\Desktop\VR Data\right_positions.txt"

df = pd.DataFrame(columns=['x','y','z'])

fig = plt.figure()
ax = plt.axes(projection='3d')

l1 = 5
l2 = 6

# Set the shoulder's position
shoulder = [0,0,0]

with open(path, 'r') as f:
    for i, row in enumerate(f):
        row  = row.split(';')
        row[-1] = row[-1][0:len(row[-1]) - 1]

        print(row)

        for j, entry in enumerate(row):
            row[j] = 10*float(entry)

        print(row)

        # Set the postion of the hand
        hand = row
        
        visualize_movement(shoulder, hand, i)

        print("\n")

        # ax.plot([k, k*k], [k, k*k], [k, k*k])
        plt.draw()
        plt.pause(1)
        ax.cla()
