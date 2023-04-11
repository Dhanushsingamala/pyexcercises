list = [3,4,2,1]
count = 0

while count<len(list[:]):
    if list[count]>2:
        list.remove(list[count])
    else:
       count+=1

print(list)
    