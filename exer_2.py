def myjoin(listname):
    delimeter = input("please enter a specific delimeter")
    return delimeter.join(listname)
    
list = ['ravi', 'ramesh', 'dhanush']

a = myjoin(list)
print(a)