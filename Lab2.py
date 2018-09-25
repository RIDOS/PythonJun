import math

x = float(input('in X():'))
y = float(input('in Y():'))
#treugol
x1 = 0
y1 = -2
x2 = 0
y2 = 3
x3 = -0.5
y3 = -3
a = (x1-x)*(y2-y1)-(x2-x1)*(y1-y)
b = (x2-x)*(y3-y1)-(x3-x2)*(y2-y)
c = (x3-x)*(y1-y3)-(x1-x3)*(y3-y)


#Krug
A = 0
B = 0
R = 2
Krug = (x-a)*(x-a)+(y-b)*(y-b)

#Pryamougol
xP1 = 0.5
yP1 = 0.5

xP2 = 0.5
yP2 = 3.5

xP3 = 3.5
yP3 = 0.5

xP4 = 3.5
yP5 = 3.5


if(a*b >= 0 and a*c >= 0):
    print('Точка пренадлежит к триугольику, но')
else:
    print('Точка не пренадлежит к триугольику, но')
if((x-A)*(x-A)+(y-B)*(y-B)<= pow(R,R) and (x>=xP2 and y>=yP3 and x<=xP3 and y<=yP2)):
    print('точка пренадлежит кругу и прямоугольнику')
else:
    print('и точка не пренадлежит кругу и прямоугольнику')