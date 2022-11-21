n = int(input())

numeros_wil = list(map(int, input().split(' ')))
numeros_edu = list(map(int, input().split(' ')))

numeros_edu.sort()
numeros_wil.sort()

jugador = 1
puntos_wil = 0
puntos_edu = 0
while len(numeros_edu) > 0 or len(numeros_wil) > 0: 
    
    if jugador == 1:
        
        if len(numeros_wil) == 0:
            numeros_edu.pop()
        
        elif len(numeros_edu) == 0:
            puntos_wil += numeros_wil[-1]
            numeros_wil.pop()
        else:
            
            if numeros_wil[-1] > numeros_edu[-1]:
                puntos_wil += numeros_wil[-1]
                numeros_wil.pop()
            else:
                numeros_edu.pop()
        
        jugador = 2
    else:
        if len(numeros_edu) == 0:
            numeros_wil.pop()
        
        elif len(numeros_wil) == 0:
            puntos_edu += numeros_edu[-1]
            numeros_edu.pop()
        else:
            
            if numeros_edu[-1] > numeros_wil[-1]:
                puntos_edu += numeros_edu[-1]
                numeros_edu.pop()
            else:
                numeros_wil.pop()
        jugador = 1
    
print(puntos_wil-puntos_edu)
