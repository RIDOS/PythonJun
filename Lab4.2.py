#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     09.10.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

f = open('Dlyalaby4.txt','r')


for num, line in enumerate(f, 1):
    if "английский" in line:
        print("Line N: " + str(num) + " : " + line.strip())
        g = open('New.txt','a+')
        g.writelines(line)
        g.close
f.close


