import re

def initialize_variables_from_namelist(namelist):
    variables = {}  # Dictionary to store variable-value pairs
    pattern = r'&\w+\s+(.+);'  # Regular expression pattern to match the assignments within the namelist
    match = re.search(pattern, namelist)  # Search for the pattern in the namelist string
    if match:
        assignments = match.group(1)  # Extract the assignment section from the match
        assignments = assignments.replace(' ', '')  # Remove any spaces from the assignments
        assignments = assignments.split(';')  # Split the assignments by semicolon (;) to get individual assignments
        for assignment in assignments:
            var, value = assignment.split('=')  # Split each assignment into variable and value
            variables[var] = eval(value)  # Evaluate the value string as a Python expression and assign it to the variable
    return variables

namelist = "&vlist v1=5.2; v2=-345; v3 = 2.2198654E+11;"
variables = initialize_variables_from_namelist(namelist)

for var, value in variables.items():
    print(f"{var}: {value}")
