import os

def prgm_available(program_name):
    pathdirs = os.environ['PATH']
    directories = pathdirs.split(';')    #stores in a list
    for each in directories:
        path = os.path.join(each , program_name)
        print(path)                 #checking paths concatenated with progm_name
        if os.path.exists(path):
            print(f'the {program_name} is found at {path}')         #stmt to print prgm found at which path
            return True
    return False

# pathdirs = os.environ['PATH']
# directories = pathdirs.split(';')

# print(directories)


if prgm_available('efficiency.txt'):
    print("program is available")
else:
    print("program is not available")