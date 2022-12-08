import json 

def parseJSON(path):
    points = []

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

        points.append(arr)
    
    return points
