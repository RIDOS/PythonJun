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
import numpy as np

n = int(input(print('n: ')))
m = int(input(print('m: ')))

a = np.arange(0,9,1).reshape(n,m)
print(a)

print()

for i in range(n):
    for j in range(m):
        a[i][j] *= a[i][j]
print(a)

print()

for i in range(len(a),0,-1):
        for j in range(1, i):
            if a[0][j-1] < a[0][j]:
                tmp = a[0][j-1]
                a[0][j-1] = a[0][j]
                a[0][j] = tmp
print(a)