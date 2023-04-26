import time 
import os

def annotate_file(filename):
    time_now = time.localtime() 
    print(time_now)
    date_now = time.strftime('%B%d_%Y',time_now)  #%b give short form %B gives complete Apr  vs April
    file ,ext = os.path.splitext(filename)
    annotated_filename = filename + '_' +date_now + ext
    return annotated_filename

b = annotate_file('dhanush.py')
print(b)