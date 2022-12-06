try:
    import sys
    import util
 
except Exception as e:
    print(f"Some imports are missing") 

def main():
    
    # name = input('What is your name? ')
    # # subprocess.run(['mono', 'home.exe', name])
    # subprocess.Popen(r"C:\Users\chloe\Downloads\UOP1_ChopChop_08alpha_Win\OpenProjects_ChopChop_0_8\Chop Chop.exe", shell=True)
    # data = requests.get

    myVar = 0

    for i in range(6):
        myVar = myVar + 1

    myVar = util.add10(myVar)

    resp = {
        "Message": "This is the json dictionary being passed back.", 
        "Data": myVar
    }

    # print(json.dumps(resp))
    print(myVar)
    sys.stdout.flush()

 
if __name__ == "__main__":
    main()    