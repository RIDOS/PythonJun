import math

x = float(input('in X: '))
y = float(input('in Y: '))

a = float(input('in A: '))
b = float(input('in B: '))

r = float(input('in R: '))

if((x-a)*(x-a)+(y-b)*(y-b)<= pow(r,r)):
    print("yes")
else:
    print("no")
