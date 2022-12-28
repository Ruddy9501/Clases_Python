n = int(input())

lista = list(map(int, input().split(' ')))

solucion = 0
cantidad_de_ceros = 0
for i in range(n):
    if lista[i] == 0:
        solucion += (i-cantidad_de_ceros)
        cantidad_de_ceros += 1

print(solucion)
