n = int(input())

cola = []
for i in range(n):
    operaciones = list(input().split(' '))
    
    if operaciones[0] == '1':
        cola.append(operaciones[1])
    else:
         cola.pop(0)
        
    print(cola[0] + " " + str(len(cola)))
