import re

def split_pathname(pathname):
    pattern = r'^(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$))' #used 3 () for groups and access dir,base name ,extension
    match = re.match(pattern, pathname)
    
    if match:
        directory = match.group(1)
        basename = match.group(2)
        extension = match.group(3)
        
        return directory, basename, extension
    else:
        return None, None, None

# usage of split_pathname function 
pathname = '/path/to/file.txt'    #example of any path 
directory, basename, extension = split_pathname(pathname)
print('Directory:', directory)
print('Basename:', basename)
print('Extension:', extension)
