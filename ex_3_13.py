import os
import sys

def cleanup_directory(directory):
    for path, dirs, files in os.walk(directory):
        for file in files:
            if 'tmp' in file:
                os.remove(os.path.join(path, file))

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <directory>')
    sys.exit(1)

directory = sys.argv[1]
if 'tmp' in directory:
    print('Error: The directory name contains "tmp"')
    sys.exit(1)

cleanup_directory(directory)
