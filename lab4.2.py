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

f=open('DlyaLaby4.txt','r')
f1=open('2.txt','w')
k=0
for i in f:
    i=i.split()
    if i[3] <= str(31):
        k+=1
        f1.write(str(i[0]+" "+i[1]+" "+i[2]+" "+i[3]+"\n"))
print(k)
f.close()
f1.close()