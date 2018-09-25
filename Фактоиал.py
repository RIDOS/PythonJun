def factorial(n):
    nach =1
    for i in range(1,n+1):
        nach*=i
    return nach
print(factorial(3))