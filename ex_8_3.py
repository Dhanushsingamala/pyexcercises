#intializing dictionary to store the commands and its values 
commands = { }

#reading input file 
file_name = 'input.txt'

with open(file_name) as file:
    for line in file:
        line=line.strip() #removing end spaces at end 
        
        if '=' in line:
            command , value = line.split('=',1) #spliting line at first occurence of '='
            command = command.strip()
            value = value.strip()
            if value:
                commands[command] = value
            else:
                print(f'Invalid line:{line}')    
        else:
            #invalid lines 
            print(f'Invalid line: {line}')  
  
#this will raise an key error if solution strategy is not found in commands            
#using this ------>solution_strategy = commands['solution strategy']  
#To avoid key error and continue using default value we can make use of get 
solution_strategy = commands.get('solution strategy')   

#printing the valid commads and values
for command, value in commands.items():
    print(f"{command}: {value}")