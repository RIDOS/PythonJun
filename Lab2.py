#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     27.11.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

x = float(input('in X():'))
y = float(input('in Y():'))

#Krug
a = 0
b = 2
R = 1

#Pryamougolnik
xP1 = 0
yP1 = -1.5

xP2 = 1
yP2 = 2


if  ((a-x)**2 + (b-y)**2 > R**2) & ((x-xP1)*(x-xP2) <= 0 and (y-yP1)*(y-yP2) <= 0) or (x <= 0 and y <= 2 and ((a-x)**2 + (b-y)**2 <= R**2)):
    print('Входит')
else:
    print('Не ходит')
