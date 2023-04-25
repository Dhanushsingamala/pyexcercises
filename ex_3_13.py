import os
import sys

def cleanup_directory(directory, files):
    for file in files:
        if 'tmp' in file:
            path = os.path.join(directory, file)
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                os.rmdir(path)
#first checks that the user has provided a directory name as a command line argument.
# If not, it prints an error message and exits
if len(sys.argv) < 2:
    print('Usage:', sys.argv[0], '<directory>')
    sys.exit(1)
# If a directory is provided, it checks if the directory name contains the substring "tmp", 
# and if it does, it prints an error message and exits.
directory = sys.argv[1]
if 'tmp' in directory:
    print('Error: The directory', directory, 'contains "tmp"')
    sys.exit(1)

os.path.walk(directory, cleanup_directory, None)  #THREE ARGS root,function,arg here arg is none since we are using for traverse

