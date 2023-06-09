import os

def findprograms(programs):
   
    installed = {}        #checks the version of installed programs if not installed throws error not innstalled
    for program in programs:
        try:
            output = os.popen(f"{program} --version", "r")
            installed[program] = True
            version = output.read()
            if "gs" in program:
                version = float(version.split()[2])
            elif "perl" in program:
                version = version.split()[3] #starts with 'this is perl' followed by version hence index[3] will access version and convert it to float and assign it to version variable
            elif "convert" in program:
                version = version.split()[2]
            elif "swig" in program:
                version = version.split()[-1]
            print(f"{program} version: {version}")
        except:
            installed[program] = False
            print(f"{program} is not installed")
    return installed


programs = ['perl','gs','convert','swig']
findprograms(programs)