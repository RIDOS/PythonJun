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

class Point:
    def __init__(self, size, width, x , y):
        self.size = size
        self.width = width
        self.x = x
        self.y = y
    def __del__(self):
        print("point is off")

class ColoredPoint( Point):
    def __init__(self, size, width, color, x, y):
        self.color = color
        Point.__init__(self, size, width, x, y)
    def __del__(self):
        print("ColoredPoint is off")

class Line( Point):
    def __init__(self, size, width, depth):
        self.depth = depth
        Point.__init__(self, size, width)
    def __del__(self):
        print("Line is off")

class ColoredLine( Line):
    def __init__(self, size, width, color):
        self.color = color
        Line.__init__(self, size, width, color, x, y)
    def __del__(self):
        print("ColoredLine is off")

class PolyLine( Line):
    def __init__(self, size, width, color, n):
        self.color = color
        self.n = n
        Line.__init__(self, size, width, color, x, y)
    def __del__(self):
        print("PolyLine is off")

class Picture:
    mass = []
    print('------------------------------------------\n')
    print('1. ColoredPoint')
    print('2. ColoredLine')
    print('3. Line')
    print('4. PolyLine')
    print('5. Point\n')
    print('------------------------------------------\n')

    but = int(input())
    if but == 1:
        size = float(input(print("SIZE:")))
        width = float(input(print("width:")))
        color = input(print("color:"))
        x = float(input(print("X:")))
        y = float(input(print("Y:")))
        a = ColoredPoint(size, width, color, x, y)
        mass.append(size)
        mass.append(width)
        mass.append(color)
        mass.append(x)
        mass.append(y)
    elif but == 2:
        size = float(input(print("SIZE:")))
        width = float(input(print("width:")))
        color = input(print("color:"))
        a = ColoredLine(size, width, color)
        mass.append(size)
        mass.append(width)
        mass.append(color)
    elif but == 3:
        size = float(input(print("SIZE:")))
        width = float(input(print("width:")))
        depth = input(print("depth:"))
        a = Line(size, width, depth)
        mass.append(size)
        mass.append(width)
        mass.append(depth)
    elif but == 4:
        n = float(input(print("N:")))
        size = float(input(print("SIZE:")))
        width = float(input(print("width:")))
        color = input(print("color:"))
        a = PolyLine(size, width, color, n)
        mass.append(size)
        mass.append(width)
        mass.append(color)
        mass.append(n)
    elif but == 5:
        size = float(input(print("SIZE:")))
        width = float(input(print("width:")))
        x = float(input(print("X:")))
        y = float(input(print("Y:")))
        a = Point(size, width, x, y)
        mass.append(size)
        mass.append(width)
        mass.append(x)
        mass.append(y)
    else:
        print('error')
    print('Mass:')
    for i in mass:
        print(i)
    print()

pr = Picture()




