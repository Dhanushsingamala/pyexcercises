import sys

#function with given parameters
def cmldict(argv, cmlargs=None, check_validity=False):
    #if cmllargs is empty creates a new one
    if cmlargs is None:     
        cmlargs = {}

    i = 0
    while i < len(argv):
        option = argv[i]
        #--option format we are checking starts with -- then finding the option from index 2
        if option.startswith('--'):
            option = option[2:]
            #to seperate the key value pairs we are using .split using '='
            if '=' in option:
                key, value = option.split('=', 1)
            else:
                key = option
                #checking and assigning value
                if i + 1 < len(argv) and argv[i+1].startswith('-') is False:
                   value = argv[i+1]
                else:
                      value = None
            #Noticing that cmlargs=None and check_validity=True is an incompatible setting
            if check_validity or key in cmlargs:
                cmlargs[key] = value
            elif check_validity:
                print(f"Invalid option: --{key}")
                sys.exit(1)
        i += 1

    return cmlargs

# Sample usage

# Define default parameters
default_params = {
    'm': 1.0,
    'b': 0.7,
    'c': 5.0,
    'func': 'y',
    'A': 5.0,
    'y0': 0.2,
    'tstop': 30.0,
    'dt': 0.05,
    'case': 'tmp1',
    'screenplot': 1
}

# Parse command-line options
cmlargs = cmldict(sys.argv[1:], cmlargs=default_params) #list of commands passed through the script here mentioned above

# Access the values
m = cmlargs['m']
b = cmlargs['b']
c = cmlargs['c']
func = cmlargs['func']
A = cmlargs['A']
y0 = cmlargs['y0']
tstop = cmlargs['tstop']
dt = cmlargs['dt']
case = cmlargs['case']
screenplot = cmlargs['screenplot']

# Print the values
print(f"m: {m}")
print(f"b: {b}")
print(f"c: {c}")
print(f"func: {func}")
print(f"A: {A}")
print(f"y0: {y0}")
print(f"tstop: {tstop}")
print(f"dt: {dt}")
print(f"case: {case}")
print(f"screenplot: {screenplot}")
