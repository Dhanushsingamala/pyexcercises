import os
import sys
import os.path as path

def findprograms(programs , directories=None):
    #checking directoried if not found fetch using os module
    if directories == None:
        directories = []
    directories += os.environ['PATH'].split(path.sep)   #path.sep is referred to as / \
    #intializing empty dictionary to store prgms as keys and path as values
    found ={}
    
    #iterating over each dir for eachprogram
    for eachprogram in programs:
        for eachdir in directories:
            Searchpath = path.join(eachdir, eachprogram)
            #checking does the path exists and it has executable permission(os.X_OK)
            if path.isfile(Searchpath) and os.access(Searchpath , os.X_OK):
                found[eachprogram] = Searchpath
                break
        #else block with for executes ,only of break not occur    
        else:
            found[eachprogram] = None
    return found



# Define the required programs and their descriptions
programs = {
    'oscillator': 'numerical ODE solver for an oscillator system',
    'gnuplot': 'plotting program',
}
directories = ['/usr/bin', '/usr/local/bin']
# Check that the required programs are available
installed = findprograms(programs.keys())
for program in installed:
    if not installed[program]:
        print(f"Error: {programs[program]} ({program}) program not found.")
    else:
        print(f'{programs[program]} is found')

