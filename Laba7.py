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

def MassIn( m ,n):
    mas = []
    r = 0
    for i in range(m):
        mas.append([])
        for j in range(n):
            mas[i].append(r)
            r+=1
    return mas

def MassOu(m, n, mas):
    print('Mass:')
    for i in range(m):
        for j in range(n):
            print("{:4d}".format(mas[i][j]), end = "")
        print()

def Dobav(m, n, mas):
    Sum = 0
    for i in range(m):
        for j in range(n):
            if mas[i][j]%2 == 0:
                Sum += mas[i][j]
    print("Sum:",Sum)
    return Sum

def OutMax(m, n, mass):
    print('X:')
    x = int(input())
    max = 0
    mi = 0
    mj = 0
    for i in range(m):
        for j in range(n):
            if mass[i][j] > max:
                max = mass[i][j]
                mi = i
                mj = j

    mass[mi][mj-1] = x
    print('Mass:')
    for i in range(m):
        for j in range(n):
            print("{:4d}".format(mass[i][j]), end = "")
        print()