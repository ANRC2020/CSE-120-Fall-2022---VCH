from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math
from math import sqrt, acos, asin, sin, atan, cos

# Clear Terminal
try: 
    import os
    clear = lambda: os. system('cls')
    clear()
except:
    pass

def law_cosine(a, b, c):
    return math.degrees(acos((c**2 - a**2 - b**2)/(-2*a*b)))

fig = plt.figure()
ax = plt.axes(projection='3d')

# Set the shoulder and end of arm points 

X_data = np.array([3, 8]) 
Y_data = np.array([5, 8])
Z_data = np.array([5, 12])

# Set the lengths of upper and lower arms
l1 = 5
l2 = 9

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

plt.show()
