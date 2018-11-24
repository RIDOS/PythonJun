#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     02.10.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

f = open('Задание1.txt')
n = f.readline().split()
max = 0
min = 222222222222
for num in n:
    if int(num) < min:
        min = int(num)
for num in n:
    if int(num) > max:
        max = int(num)

f.close
print('Максимальный элемет:')
print(max)
print('Минимальный элемет:')
print(min)


