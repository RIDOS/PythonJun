import math
# ТОЧКА
x = float(input('in X: '))
y = float(input('in Y: '))
# РАДИУС
r = float(input('in R: '))
# ЦЕНТЫ ОКУЖНОСТИ
a = float(input('in A: '))
b = float(input('in B: '))
# Условие(Входит ли в окружость)
if((x-a)*(x-a)+(y-b)*(y-b)<=r*r):
    print('Пренадлежит окружности')
else:
    print('Не пренадлежит окружности')