#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     09.12.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

file = open('Read.txt', 'r')
n = file.readline().split()

sum = 0
sred = 0

for num in n:
    sum += int(num)

sred = sum / len(n)

print('Sum  :', sum)
print('Sred :', sred)


file1 = open('Writer.txt', 'w+')
file1.writelines('Sum:\t' + str(sum) + ';\n'+'Sred:\t' + str(sred) + ';')


print('\nWriter is worked')

file1.close()
file.close()
