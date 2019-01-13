#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     26.11.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

f = open('Задание1.txt','r')
n = f.readline().split()

sum = 0
sred = 0

for num in n:
    sum += int(num)

sred = sum / len(n)

print('Sum  :', sum)
print('Sred :', sred)

















