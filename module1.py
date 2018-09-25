#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     25.09.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import numpy as np
import random

#arg1 = float(input(print('arg1 = ')))
#op = input('znak: ')
#arg2 = float(input(print('arg2 = ')))



def Arifme(arg1,arg2,op):
    if op == '*':
        return arg1 * arg2
    elif op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '/':
        return arg1 / arg2
#print(Arifme(arg1,arg2,op))

def sqrt(a):
    p = 4*a
    s = a**2
    diag = a*math.sqrt(2)
    return p, s, diag
#print (sqrt(5))

##z = np.zeros(10)
##print(z)
##z = np.full(10,2.5)
##print(z)

z = np.random.random((3,3,3))
##print(z)
z = np.arange(9).reshape(3,3)
##print(z)
z = np.random.random((10,10))
print(z)
print(z.mean()) ## среднее значение
print(z.min())
print(z.max())
