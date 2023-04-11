arglist = [
    'filename' , 'plottitle' ,'psfile']

filename = arglist[0]
plottitle = arglist[1]
psfile = arglist[2]

start = 0
stop =  len(arglist)
step = 1

for index in range(start,stop,step):
    print ('arglist[%d]=%s'  %(index , arglist[index]) )
