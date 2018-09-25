n = 4
a = []
for i in range(n):
    a.append([0]*n)
for i in range(n):
    for j in range(n):
        if i>j:
            a[i][j]=2
        a[i][i]=1
print(a)