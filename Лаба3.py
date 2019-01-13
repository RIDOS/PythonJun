#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     19.12.2018
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
        mas[i].append(r)
        r+=1

Sum = 0
Proiz = 10000

for i in range(m):
    for j in range(n):
        if mas [i][j] %2 == 0:
            Sum += mas[i][j]
            Proiz *= mas[i][j]

print('Mass:')
for i in range(m):
    for j in range(n):
        print("{:4d}".format(mas[i][j]), end = "")
    print()

print('\nSum:', Sum)
print('Proizvedenie:', Proiz)

Pr = 1
for i in range(m):
        Pr *= mas[i][i]
print('\nPr:', Pr)