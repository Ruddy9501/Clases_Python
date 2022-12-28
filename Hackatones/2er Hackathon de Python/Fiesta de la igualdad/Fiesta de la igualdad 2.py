n = int(input())
lis = list(map(int, input().split(' ')))

maximo = max(lis)
solucion = 0
for x in lis:
    solucion += maximo-x

print(solucion)