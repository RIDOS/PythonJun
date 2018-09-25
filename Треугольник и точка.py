def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0


x = float(input('in X0:'))
y = float(input('in Y0:'))


x1 = -0
y1 = -3
x2 = -0.5
y2 = 3
x3 = -0
y3 = -2.5
a = (x1-x)*(y2-y1)-(x2-x1)*(y1-y)
b = (x2-x)*(y3-y1)-(x3-x2)*(y2-y)
c = (x3-x)*(y1-y3)-(x1-x3)*(y3-y)

if(sign(a) == sign(b) == sign(c)):
    print('Точка пренадлежит области')
else:
    print('Точка не пренадлежит области')