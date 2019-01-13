#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     10.12.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Lab7

m = 5
n = 5

a = Lab7.MassIn(m, n)

Lab7.MassOu(m, n, a)

print('\nProiz:',Lab7.MoDUL(m, n, a))
print()
x = int(input(print('X =')))
Lab7.OutMax(m, n, a, x)
print('\n')

Lab7.MoDUL(m, n, a)
Lab7.MassOu(n, m, a)