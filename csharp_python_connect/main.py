import subprocess

def main():
    name = input('What is your name? ')
    # This runs a C# file given file path with string arguments
    # verified on Shreya's mac
    # subprocess.run(['mono', 'home.exe', name])
    
    # TODO: Get final Unity exe
    # TODO: Finalize/Verify string args to pass patient name
    
    # This launches a Unity exe application from command prompt with no additional string arguments
    # Verified on Chloe's windows - works on Command prompt and powershell, not ubuntu
    subprocess.Popen(r"C:\Users\chloe\Downloads\UOP1_ChopChop_08alpha_Win\OpenProjects_ChopChop_0_8\Chop Chop.exe", shell=True)

if __name__ == "__main__":
    main()    