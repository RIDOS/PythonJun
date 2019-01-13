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

m = int(input(print('M:')))
n = int(input(print('N:')))

r = 1
mas = []

for i in range(m):
    mas.append([])
    for j in range(n):
        mas[i].append(r*2)
        r+=1

print('Mass:')
for i in range(m):
    for j in range(n):
        print("{:4d}".format(mas[i][j]), end = "")
    print()

print('\n'*2)
k = 0
for i in range(m):
    if (mas[0][i] > mas[1][i] > mas[2][i]) or (mas[0][i] < mas[1][i] < mas[2][i]):
        k = i
        break
print('В стоке: {} масив возастает, либо убывает'.format (str(k)), end = '')


for i in range(n):
    mas[i][i], mas[n - i -1][i] = mas[n - i - 1][i], mas[i][i]

print('\nMass:')
for i in range(m):
    for j in range(n):
        print("{:4d}".format(mas[i][j]), end = "")
    print()


