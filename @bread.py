#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Азат
#
# Created:     09.11.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##class A:
##    y = 10
##    def __init__(self, n):
##        self.n = n
##
##z = A()


##def f_bread(func):
##    def wrapper():
##        print("func:")
##        func()
##        print("end.")
##    return wrapper
##def ingredients(func):
##    def wrapper():
##        print("tomato")
##        func()
##        print("bacon")
##    return wrapper
##def sandwich(food = "bread"):
##    print(food)


def bread(func):
    def wrapper():
        print("func:")
        func()
        print("end.")
    return wrapper
def ingredients(func):
    def wrapper():
        print("tomato")
        func()
        print("bacon")
    return wrapper
@bread
@ingredients

def sandwich(food = "bread"):
    print(food)

sandwich()