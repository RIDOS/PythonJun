x1 = float(input('in X1:'))
y1 = float(input('in Y1:'))
x2 = float(input('in X2:'))
y2 = float(input('in Y2:'))
x3 = float(input('in X3:'))
y3 = float(input('in Y3:'))

x0 = float(input('in X0:'))
y0 = float(input('in Y0:'))

a = (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)
b = (x2-x0)*(y3-y1)-(x3-x2)*(y2-y0)
c = (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)

if(a*b >= 0 and a*c >= 0):
    print('Точка пренадлежит области')
else:
    print('Точка не пренадлежит области')