#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     19.12.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

x = float(input('in X():'))
y = float(input('in Y():'))
#treugol
x1 = 2
y1 = 1
x2 = 0
y2 = 6
x3 = -2
y3 = 1
a = (x1-x)*(y2-y1)-(x2-x1)*(y1-y)
b = (x2-x)*(y3-y1)-(x3-x2)*(y2-y)
c = (x3-x)*(y1-y3)-(x1-x3)*(y3-y)

Tr = (a*b >= 0 and a*c >= 0)
#Krug---------------------------------------------------------------------------
A = 3.5
B = 0
R = 2
Kr = (x-a)*(x-a)+(y-b)*(y-b)

#Pryamougol---------------------------------------------------------------------
xP1 = -3
yP1 = 2.5

xP2 = 3
yP2 = 0.5

Pr = (x>=xP1 and y>=yP2 and x<=xP2 and y<=yP1 )

if ( Tr and Pr and x < 0) or ( Kr and Pr and not Tr):
    print('Входит')
else:
    print('Не входит')

