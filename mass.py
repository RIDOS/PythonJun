a = 3# kol stolb
b = 5# kol strok
r = 0
mas=[]#Обьявляем массив
for i in range(a):#Походим по массиву(по строкам)
    mas.append([])#Включеие массива
    for j in range(b):
        mas[i].append(r)
        r+=1
print(mas)