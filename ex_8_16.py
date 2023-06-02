import re

def gettime(text):
#groups                                1     2     3
    time_pattern = r"Date/Time\s+:\s+(\d+):(\d+):(\d+)"
    date_pattern = r"Date/Time\s+:\s+(\d+):(\d+):(\d+)"   #\d int +one or more occurence of lastelement
    
    time_match = re.search(time_pattern, text)
    date_match = re.search(date_pattern, text)
    
    #if matches found then creating respecyive tuples using indexing
    if time_match and date_match:
        time_tuple = (time_match.group(1), time_match.group(2), time_match.group(3))
        date_tuple = (date_match.group(1), date_match.group(2), date_match.group(3))
        return time_tuple, date_tuple
    else:
        return None


def prefix(time_tuple, date_tuple, filename):
    if time_tuple and date_tuple:
        #to get the deside format as given in ex 8.16 2002_05_19__18_10_03__img_4978.jpg
        prefix_str = f"{date_tuple[0]}_{date_tuple[1]}_{date_tuple[2]}__{time_tuple[0]}_{time_tuple[1]}_{time_tuple[2]}__"
        #checking if file name already start with given format if yes returning filename else adding prefix to filename
        if filename.startswith(prefix_str):
            return filename
        else:
            return prefix_str + filename
    else:
        return filename
    
    
# Sample text from jhead output as give in doct
text = """
File name : tmp2.jpg
File size : 179544 bytes
File date : 2003:03:29 10:58:40
Camera make : Canon
Camera model : Canon DIGITAL IXUS 300
Date/Time : 2002:05:19 18:10:03
Resolution : 1200 x 1600
Flash used : Yes
Focal length : 11.4mm (35mm equivalent: 79mm)
CCD width : 5.23mm
Exposure time: 0.017 s (1/60)
Aperture : f/4.0
Focus dist. : 1.17m
Exposure bias:-0.33
Metering Mode: matrix
Jpeg process : Baseline
"""

# Extract time and date
time_tuple, date_tuple = gettime(text)

# Original filename
filename = "img_4978.jpg"

# Prefix the filename
prefixed_filename = prefix(time_tuple, date_tuple, filename)

print(prefixed_filename)

