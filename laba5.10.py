#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     07.12.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Progression:
    def __init__(self, n):
        self.n = n




class Linear(Progression):
    def __init__(self, a1, an, d, n):
        self.a1 = a1
        self.an = an
        self.d = d
        Progression.__init__(self, n)

    def Sum(self):
        N = self.n
        Sum = ((self.a1 + self.an)/(2)) * N
        return Sum

    def Elem(self):
        N = self.n
        an = ((2 * self.a1 + (N - 1) * self.d) / (2)) * N
        return an

class Exceptional(Progression):
    def __init__(self, b1, q, n, bn):
        self.b1 = b1
        self.q = q
        self.bn = bn
        Progression.__init__(self, n)

    def Sum(self):

            N = self.n
            Sum = ((self.b1 * (1 - pow(self.q, N)))/(1 - self.q))
            return Sum

    def Elem(self):
        if self.q != 1:
            N = self.n
            an = ((self.b1 - self.q * self.bn) / (1 - self.q))
            return an


#Test --- Linear - Exceptional ---->


print('---------- \t Linear \t -----------\n')
A = Linear(3, 8, 4, 4)
print('Sum:', A.Sum(),'\n')
print('Elem:', A.Elem())
##print('\n')


print('--------\tExceptional \t--------\n')
B = Exceptional(4, 3, 8, 20)
print('Sum:', B.Sum(),'\n')
print('Elem:', B.Elem())
print('------------------------------------\n')


class Series:
    m = 2
    n = 8

    r = 0
    mas = [[0] * 2] * 2

    def Input(self, sum, elem):

        for i in range(self.m):
            for j in range(self.n):
                self.mas[i][0] = elem
                self.mas[i][1] = sum

    def Output(self):
    ##        for i in range(self.n):
    ##            for j in range(self.m):
    ##                print("{}".format(self.mas[i][j]), end = " ")
                print(self.mas)
    def IputFile(self):
        doc = open('Progression.txt', 'w+')
        doc.write(self.mas)
        doc.close()







#Test --- Input - InFile ---->


print('----------- \t Input \t -----------\n')

qwerty = A.Sum()
asdfgh = A.Elem()

qwerty1 = B.Sum()
asdfgh1 = B.Elem()

b = Series()

b.Input(qwerty, asdfgh)

b.Output()

print('\n--------\t Input File \t--------\n')
try:

    b.IputFile()
    print('OK')
except Exception:
    print('Error')


print('------------------------------------\n')
print()