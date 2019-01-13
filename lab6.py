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

class Sladosti():
    def __init__( self, kol, proiz):
        self.kol = kol
        self.proiz = proiz
    def __del__(self):
        print("Candy was born!")

class Cookie(Sladosti):
    def __init__(self, prazdnik, kol, proiz):
        self.prazdnik = prazdnik
        Sladosti.__init__( self, kol, proiz)
    def __del__(self):
        print("Пазднечные печеньки к {}. Всего печенья - {}".format(self.prazdnik, self.kol))

class Chocolate(Sladosti):
    def __init__(self, Nazvanie, kol, proiz):
        self.Nazvanie = Nazvanie
        Sladosti.__init__( self, kol, proiz)
    def __del__(self):
        print("Шоколд {}. Всего на складе  = {}".format(Nazvanie, self.kol))

class SNach(Cookie):
    def __init__(self, nachinka, prazdnik, kol):
        self.nachinka = nachinka
        self.prazdnik = prazdnik
        self.kol = kol
    def __del__(self):
        print("Начинка: {}".format(self.nachinka))

class BNach(Cookie):
    def __init__(self, testo):
        self.testo = testo
    def __del__(self):
        print("Печеьки из {} теста, тающие во рту...".format(self.testo))

class Black(Chocolate):
    def __init__(self, ProcGor):
        self.ProcGor = ProcGor
    def __del__(self):
        print("Черный шоколад, процент горькости - {}%".format(self.ProcGor))

class White(Chocolate):
    def __init__(self, nachin):
        self.nachin = nachin
    def __del__(self):
        print("Белый шоколад, с начинкой {}.".format(self.nachin))

SladostiFile = open("CandyWorld.txt",'w+')
nach = input(print("Введите начинку для шоколада:"))
prazd = input(print("К какому прзднику подготовить печенье: "))
Kol = input(print("Количество печенья: "))

Cook = SNach(nach, prazd, Kol)
print()
print("Печеье с начинкой {} к празднику {} готово. Всего на складе - {}".format(Cook.nachinka, Cook.prazdnik, Cook.kol))
print()
SladostiFile = SladostiFile.write("Печеье с начинкой {} к празднику {} готово. Всего на складе - {}".format(Cook.nachinka, Cook.prazdnik, Cook.kol))
print("Запись в фаил...")
print("Конец программы")