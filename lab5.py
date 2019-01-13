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



class Vehicle:
    def __init__(self, Sum, Date, Speed):
        self.Date = Date
        self.Sum = Sum
        self.Speed = Speed

    def __del__(self):
        print('Vehicle out')

class Car(Vehicle):
    def __init__(self, Sum, Date, Speed, Marka, Tip):
        Vehicle.__init__(self, Sum, Date, Speed)
        self.Marka = Marka
        self.Tip = Tip
    def Print(self):
        print('Ценна:' + self.Sum +'\nГод выпуска:' + self.Date + '\nТип автомобиля:' + self.Tip + '\nМарка автомобиля:' + self.Marka)

class Bicycle(Vehicle):
    def __init__(self, Sum, Date, Speed, Marka, Tip, TipWhell):
        Vehicle.__init__(self, Sum, Date, Speed)
        self.Marka = Marka
        self.Tip = Tip
        self.TipWhell = TipWhell
    def Print(self):
        print('Ценна:' + self.Sum +'\nГод выпуска:' + self.Date + '\nТип велосипеда:' + self.Tip + '\nМарка велосипеда:' + self.Marka + '\nТип пакрышки:'+ self.TipWhell)

class Lorry(Vehicle):
    def __init__(self, Sum, Date, Speed, Marka, Tip, VGruzop):
        Vehicle.__init__(self, Sum, Date, Speed)
        self.Marka = Marka
        self.Tip = Tip
        self.VGruzop= VGruzop
    def Print(self):
        print('Ценна:' + self.Sum +'\nГод выпуска:' + self.Date + '\nТип грузовика:' + self.Tip + '\nМарка грузовика:' + self.Marka + '\nГрузоподемность:' + self.VGruzop)


#-------------------------------------------------------------------------------

class Garage:

    def InputVehicle(garage):
        garage = []
        print('------------------------------------------\n')
        print('1. Машина')
        print('2. Велосипед')
        print('3. Грузовая машина\n')
        print('------------------------------------------\n')

        but = int(input())

        if but == 1:
            a = iCar()
            garage.append(str(a.Date))
            garage.append(str(a.Marka))
            garage.append(str(a.Speed))
            garage.append(str(a.Sum))
            garage.append(str(a.Tip))
        elif but == 2:
            b = iBicycle()
            garage.append(b.Date)
            garage.append(b.Marka)
            garage.append(b.Speed)
            garage.append(b.Sum)
            garage.append(b.Tip)
            garage.append(b.TipWhell)
        elif but == 3:
            c = iLorry()
            garage.append(c.Date)
            garage.append(c.Marka)
            garage.append(c.Speed)
            garage.append(c.Sum)
            garage.append(c.Tip)
            garage.append(c.VGruzop)
        else:
            print('Error')

def iCar():
    print('Машина:')
    s = input(print('Введите цену машины:'))
    g = input(print('Введите год выпуска:'))
    sd = input(print('Введите максимальную скорость автомобиля:'))
    m = input(print('Введите марку машины:'))
    tip = input(print('Введите тип машины:'))

    a = Car(s, g, sd, m, tip)

    print('------------------------------------------\n')
    return a

def iBicycle():
    print('Велосипед:')
    s = input(print('Введите цену влосипеда:'))
    g = input(print('Введите год выпуска:'))
    sd = input(print('Введите максимальную скорость велосипеда:'))
    m = input(print('Введите марку велосипеда:'))
    tip = input(print('Введите тип велосипеда:'))
    tipW = input(print('Введите тип протектора:'))

    b = Bicycle( s, g, sd, m, tip, tipW)

    print('------------------------------------------\n')
    return b

def iLorry():
    print('Грузовой автомобиль:')
    s = input(print('Введите цену машины:'))
    g = input(print('Введите год выпуска:'))
    sd = input(print('Введите максимальную скорость гузового автомобиля:'))
    m = input(print('Введите марку гузовой машины:'))
    tip = input(print('Введите тип гузовой машины:'))
    ves = input(print('Введите грузоподъемность:'))

    c = Lorry(s, g, sd, m, tip, ves)

    print('------------------------------------------\n')
    return c

def Output(mass):
    print('Mass:')
    for i in range(len(mass)):
        print(mass[i])

def Sorted(mass):
    mass = sorted(mass)


#-------------------------------------------------------------------------------
mas = []
Garage.InputVehicle(mas)
print()
Output(mas)


