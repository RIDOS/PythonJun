#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Азат
#
# Created:     27.11.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Igrushki():
    def __init__(self, kol, made_in):
        self.kol = kol
        self.made_in = made_in
    def __del__():
        print('Igrushki is offline')

class Shotgun(Igrushki):
    def __init__(self, model, patrons):
        self.model = model
        self.patrons = patrons
        Igrushki.__init__(kol, made_in)
    def __del__():
        print('Shotgun is offline')

class Mashinki(Igrushki):
    def __init__(self, model, marka):
        self.model = model
        self.marka = marka
        Igrushki.__init__(kol, made_in)
    def __del__():
        print('Mashinki is offline')

class Auto(Shotgun):
    def __init__(self, vmestimost, priklad):
        self.vmestimost = vmestimost
        self.priklad = priklad
        Shotgun.__init__(model, patrons)
    def __del__():
        print('Autoshotgun is offline')

class Pompow(Shotgun):
    def __init__(self, ves, skorost):
        self.ves = ves
        self.skorost = skorost
    def __del__():
        print('Pompowshotgun is offline')

class Gonoc(Mashinki):
    def __init__(self, kolsedenev, dvigatel, model, marka):
        self.kolsedenev = kolsedenev
        self.dvigatel = dvigatel
        self.marka = marka
        self.model = model
    def __del__():
        print('Gonocnii mashinki is offline')

class Voennie(Mashinki):
    def __init__(self, bronya, komufljag):
        self.bronya = bronya
        self.komufljag = komufljag
        Mashinki.__init__(model, marka)
    def __del__():
        print('Voennie mashinki is offline')


a = Gonoc(4, 'v8', 'tt', 'audi')
print('\n--------------Гоночный автомобиль------------------\n')
print('Марка автомобиля:',a.marka)
print('Модель автомобиля:',a.model)
print('Двигаетль автомобиля:',a.dvigatel)
print('Кол-во сиденьев в автомобиле:',a.kolsedenev)
print('\n---------------------------------------------------\n')




