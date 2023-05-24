import sys 
import os
import re 

#checking if required command line arguments are provided or not 
if len(sys.argv)<3:
    print('format unexpected ,required  format is  python grep.py pattern file1 file2 file3 ...')
    sys.exit(1)
    
#extracting the file name and pattern provided from command line 
pattern = sys.argv[1]
file_names = sys.argv[2:]

#iterating over the file names
for file in file_names:
    
    #check if file exists 
    if not os.path.isfile(file):
        print(f"file '{file}' not found in directory")
        continue
    
    #if file exists , opening the file and read its lines 
    with open(file ,'r') as f:
        lines = f.readlines()
        
    #iterating over the lines and find matches for the pattern 
    line_number =1
    for line in lines:
        match = re.search(pattern,line)
        if match:
            #print the matched line with the file name and line number
            print(f"{file} : {line_number} : {line.strip()}")
        line_number+=1
        
    
