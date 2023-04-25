import os
import sys
import glob    #The glob module, which is short for global, is a function that's used to search for files that match a specific file pattern or name
from PIL import Image

directories = os.sys.argv[1:] # 0 index have name itself , rest used ro pass command line arguments in python

for dir in directories:
    os.chdir(dir)   #used to change the directory to current dir
    #using glob here * indicates all for all .png files in directory
    for pngfile in glob.glob('*.png'):
        #changing names of files by spliting name and extension appending .gif 
        giffile = os.path.splitext(pngfile)[0] + '.gif'
        #changing the format using PIL-> image
        Image.open(pngfile).save(giffile)
