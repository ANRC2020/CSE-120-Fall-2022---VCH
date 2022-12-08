import json 

import math
from math import sqrt, acos, asin, sin, atan, cos, pi

def parseJSON(path):
    points = []
    times = []
    with open(path, 'r') as f:

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
        points.append(arr)
    
    return points, times


def euclidean_distance(point_1, point_2):
    distance = sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2 + (point_1[2] - point_2[2])**2)

    return distance

def law_cosine(a, b, c):
    return math.degrees(acos((c**2 - a**2 - b**2)/(-2*a*b)))

def velocity(prev_angle, curr_angle, prev_time, curr_time, length):
    radians = ((curr_angle - prev_angle)/180)*pi
    
    return abs(radians/(curr_time - prev_time)*length)
