import re

real = r'\s*(?P<number>-?(\d+(\.\d*)?|\d*\.\d+)([eE][+\-]?\d+)?)\s*'
c = re.compile(real)
some_interval = '[3.58652e+05 , 6E+09]'
groups = c.findall(some_interval)
print(groups)
lower = float(groups[0][c.groupindex['number']])  # Access the match 
upper = float(groups[1][c.groupindex['number']])  # Access the match

print(f'lower limit: {lower}')
print(f'upper limit :{upper}') 

