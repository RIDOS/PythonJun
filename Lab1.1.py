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

list = []
sum = 0
for i in range(4, 33):
    list.append(i + 10)
    sum += i+10

print('List :', list)
print('Len  :', len(list))
print('Sum  :', sum)

print('\n-------DELET-------\n')
del list
print(list)
print('\n-------SUCCESS-----\n')
