import os
import os.path as path

def findprograms(programs , directories=None):
    #checking directoried if not found fetch using os module
    if directories == None:
        directories = []
    directories += os.environ['PATH'].split(path.sep)
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


programs = {
    'gnuplot.exe': 'plotting program',
    'gs.exe': 'ghostscript, ps/pdf converter and previewer',
    'f2py.exe': 'generator for Python interfaces to Fortran',
    'swig.exe': 'generator for Python interfaces to C/C++',
    'convert.exe': 'image conversion, part of the ImageMagick package',
}

#storing programs dict keys in installed as iterable list 
installed = findprograms(programs.keys())
for program in installed:
    if installed[program]:
        print('You have %s (%s)' % (program, programs[program]))
    else:
        print('*** Program', program, 'was not found')
        print(' .....(%s)' % programs[program])

