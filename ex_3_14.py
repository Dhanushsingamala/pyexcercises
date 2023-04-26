import os
import shutil
import time

def find_old_large_files(root, size_limit_mb, days_limit):
    # Calculate the cutoff time for file access time
    timelast = time.time() - (days_limit * 24 * 60 * 60)
    print(timelast)   #unix time stamp only gets no of seconds
    print(f"Cutoff time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timelast))}") #we can get in time format

    # List to hold the filenames that meet the test criteria
    file_list = []

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)

            # Check if the file meets the size and access time criteria
            if os.path.getsize(file_path) > size_limit_mb * 1024 * 1024 and os.path.getatime(file_path) < timelast:
                # Copy the file to a new location before deleting
                shutil.copy(file_path, os.path.join(root, 'old_large_files', filename))  #copying
                os.remove(file_path)
                file_list.append(os.path.join(root, 'old_large_files', filename))

    # Return the list of old and large files
    return file_list

files = find_old_large_files('C:\\Users\\DHANU\\Desktop\\Tseminar',5,14)
print(files)

