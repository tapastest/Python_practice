import datetime

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

list_two = [2,98,99,88,90,76]

path = "D:\python2.txt"
with open(timeStamped'.txt','w') as outf:
    outf.write(list_two)

