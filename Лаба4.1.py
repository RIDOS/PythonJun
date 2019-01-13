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

f = open('Задание1.txt')
a = open('Writer.txt', 'w')
n = f.readline().split()
max = 0
min = 222222222222
for num in n:
    if int(num) < min:
        min = int(num)
for num in n:
    if int(num) > max:
        max = int(num)


print('Максимальный элемет:')
print(max)
print('Минимальный элемет:')
print(min)



a = a.write("Min - " + str(min) + '\n' + "Max - " + str(max))


f.close()