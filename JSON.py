#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     16.11.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import shutil


##shutil.copy('mio.txt', 'mio2.txt')
##shutil.copy2('mio.txt', 'mio2.txt')

##shutil.copytree('C:\\New', 'D:\\')

F = open('mio.txt', 'r')
a = open('mioBin.bin','ab+')
print('Имя файла: ', F.name)
print('В каком режиме был откыт файл: ', F.mode)

print('')

print('Имя файла: ', a.name)
print('В каком режиме был откыт файл: ', a.mode)
print('')


for i in F.readline():
    l = i
    a.write(l)


F.close()
a.close()
print('Файл закрыт: ', F.closed)
print('Файл закрыт: ', a.closed)
print('Программа выполненна...')

##shutil.rmtree('C:\\New')