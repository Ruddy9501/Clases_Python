n = int(input())

pila = []
for i in range(n):
    lis = list(map(int, input().split(' ')))
    
    if lis[0] == 1:
        pila.append(lis[1])
    else:
        pila.pop()
        
    print(str(pila[-1]) + ' ' + str(len(pila)))
