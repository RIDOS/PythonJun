#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Азат
#
# Created:     28.11.2018
# Copyright:   (c) Азат 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from tkinter import *


root = Tk()

button1 = Button(root, text = u'1', width=8, height = 4)
button2 = Button(root, text = u'2', width=8, height = 4)
button3 = Button(root, text = u'3', width=8, height = 4)

button4 = Button(root, text = u'4', width=8, height = 4)
button5 = Button(root, text = u'5', width=8, height = 4)
button6 = Button(root, text = u'6', width=8, height = 4)

button7 = Button(root, text = u'7', width=8, height = 4)
button8 = Button(root, text = u'8', width=8, height = 4)
button9 = Button(root, text = u'9', width=8, height = 4)

button10 = Button(root, text = u'0', width=8, height = 4)
button16 = Button(root, text = u'.', width=8, height = 4)
button11 = Button(root, text = u'C', width=8, height = 4)

button12 = Button(root, text = u'+', width=8, height = 4)
button13 = Button(root, text = u'-', width=8, height = 4)
button14 = Button(root, text = u'*', width=8, height = 4)
button15 = Button(root, text = u'/', width=8, height = 4)

button17 = Button(root, text = u'=', width=50, height = 2)

label1 = Label(root, width=50)
entry1 =  Entry(root, width=50, bd = 20)

##entry1.place(x = '10', y = '10')
##button1.place(x = '1', y = '5')
##button2.place(x = '-20', y = '5')
##button3.place(x = '40', y = '30')
##button17.place(x = '20', y = '30')

entry1.grid(row = 0, column = 0, columnspan = 5)
label1.grid(row = 1, column = 0, columnspan = 5)

button1.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)
button3.grid(row = 4, column = 2)
button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)
button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)

button10.grid(row = 5, column = 0)
button16.grid(row = 5, column = 1)
button11.grid(row = 5, column = 2)

button12.grid(row = 2, column = 3)
button13.grid(row = 3, column = 3)
button14.grid(row = 4, column = 3)
button15.grid(row = 5, column = 3)

button17.grid(row = 6, column = 0, columnspan = 4)

root.mainloop()


button1.bind('<Button - 1>', label1 = '1')
button2.bind('<Button - 2>', label1 = '2')
button3.bind('<Button - 3>', label1 = '3')
button4.bind('<Button - 4>', label1 = '4')
button5.bind('<Button - 5>', label1 = '5')
button6.bind('<Button - 6>', label1 = '6')
button7.bind('<Button - 7>', label1 = '7')
button8.bind('<Button - 8>', label1 = '8')
button9.bind('<Button - 9>', label1 = '9')
button10.bind('<Button - 10>', label1 = '0')























##root = Tk()
##text1 = Text(root, height = 7, width = 7, font = 'Arial 14', wrap = WORD)
##
##text1.pack()
##root.mainloop()
##def leftklick(root):
##    print(' Вы нажали левую кнопку мыши')
##def rightklick(root):
##    print(' Вы нажали правую кнопку мыши')
##button1 = Button(root, text = u'Нажми')
##button1.pack()
##button1.bind('<Button-1>', leftklick)
##button1.bind('<Button-3>', rightklick)
##root.mainloop()

##button1 = Button(root, text = 'OK', width = 25, height = 5, bg = 'black', fg = 'red', font = 'arial 14')
##button1.pack()
##root.mainloop()
