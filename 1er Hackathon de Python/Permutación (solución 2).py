n = int(input())
lista = list(map(int, input().split(' ')))

lista = set([x for x in lista if x <= n])

print (n - len(lista))
