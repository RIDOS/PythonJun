import math

x = float(input('in X: '))
y = float(input('in Y: '))
if(y>=x*x and y<=1 and x<=0):
    print('Прнадлежит')
else:
    print('Не прнадлежит')