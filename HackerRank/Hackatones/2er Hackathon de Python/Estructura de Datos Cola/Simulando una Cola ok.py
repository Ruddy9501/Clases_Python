n = int(input())

cola = []
posicion = 0
for i in range(n):
    operaciones = list(input().split(' '))
    
    if operaciones[0] == '1':
        cola.append(operaciones[1])
    else:
        posicion += 1
        
    print(cola[posicion] + " " + str(len(cola) - posicion))