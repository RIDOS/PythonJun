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
f=open('Dlyalaby4.txt','r')
f1=open('lab4.2.txt','w+')
k=0
for i in f:
    i = i.split()
    if (i[1] == "английский"):
        k+=1
        f1.write(str(i[0] + " " + i[1]+" "+ i[2] + " " + i[len(i)-1] + "\n"))
print(k)
f.close()
f1.close()