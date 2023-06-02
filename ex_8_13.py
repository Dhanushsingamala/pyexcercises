import re

def findall(pattern, string):
    matches = []          #empty list to store matches 
    match = re.search(pattern, string)   
    
    while match:
        matches.append(match.group())       #adding the match to list 
        string = string[match.end():]       #slicing the end of match word
        match = re.search(pattern, string)  #after completion restarting the search 
    
    return matches    

# Example usage of the generated find all fun
pattern = r'-?\d+(\.\d+)?'
string = '3.29 is a number, -4 and 3.28E+00 too'   #given string in doc
numbers = findall(pattern, string)
print(numbers)
