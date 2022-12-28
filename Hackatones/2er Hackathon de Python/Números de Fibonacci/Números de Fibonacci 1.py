n = int(input())

if n == 1:
    print (1)
elif n == 2:
    print(2)
else:
    x1 = 1
    x2 = 1
    for i in range (2, n):
        x3 = x1+x2
        x1 = x2
        x2 = x3
    print(x3)
