n = int(input())
lista = list(map(int, input().split(' ')))

solucion = 0
for i in range(1, n+1):
    if i not in lista:
        solucion += 1

print(solucion)
