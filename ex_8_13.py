import re

def findall(pattern, string):
    matches = []
    match = re.search(pattern, string)
    
    while match:
        matches.append(match.group())
        string = string[match.end():]
        match = re.search(pattern, string)
    
    return matches

# Example usage
pattern = r'-?\d+(\.\d+)?'
string = '3.29 is a number, -4 and 3.28E+00 too'
numbers = findall(pattern, string)
print(numbers)
