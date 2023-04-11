def exjoin(*args):
    result = ''
    delimeter=input("please enter specific delimeter u want to join:\n")
    for arg in args:
        if isinstance(arg,str):
            result += arg
            result+=delimeter
        if isinstance(arg,(list,tuple)):
            result += delimeter.join(arg)
    return result

#following args are give in doc exercise

list1 = ['s1', 's2', 's3']
tuple1 = ('s4', 's5')
ex1 = exjoin(' ', 't1', 't2', list1, tuple1, 't3', 't4')

print(ex1)