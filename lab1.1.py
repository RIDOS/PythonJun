#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     08.12.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


list = []
sum = 0
for i in range(4, 30):
    if i% 2 != 0:
        list.append(i + 4)

print('List :', list)
print('Min  :', min(list))
print('Max  :', max(list))
