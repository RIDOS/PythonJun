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
root.title("Calculator")
root.minsize(325, 230)
root.resizable( width = False, height = False)

#------------ Создание кнопок лейбла, для вывода входного числа, и строки ввода ------------
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

label1 = Label (width=50)
entry1 =  Entry (width=50, bd = 20)
#------------ Положение кнопок на форме ------------
##entry1.place(x = '10', y = '10')
##button1.place(x = '1', y = '5')
##button2.place(x = '-20', y = '5')
##button3.place(x = '40', y = '30')
##button17.place(x = '20', y = '30')
#------------ Вывод лейбла, кнопок и строки ввода на форму ------------
entry1.grid(row = 0, column = 0, columnspan = 5)
label1.grid(row = 8, column = 0, columnspan = 5)

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
#------------ Отображение самой формы ------------
root.mainloop()
#------------ Создание биндов ------------
##button1.bind('<Button - 1>', label1(text = '1'))
#------------ Логика ------------
def calc(key):
    global memory
    if key == "=":
        str1 = "-+0123456789.*/"
        if entry1.get() [0] not in str1:
            entry1.insert(END, "First symbol is not number!")
        try:
            result = eval(entry1.get())
            #eval - функция, выполняющая все вычисления
            entry1.insert(END, "=" + str(result))
        except:
            entry1.insert(END, "Error!")
    elif key == "C":
            entry1.delete(0, END)

calc(root)






















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
