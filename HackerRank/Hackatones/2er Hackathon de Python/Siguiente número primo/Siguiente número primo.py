n = int(input())

marcador = False
while marcador == False:
    n += 1
    
    marcador = True
    
    for x in range(2, int(n**(0.5) + 1)):
        if n % x == 0:
            marcador = False
            
print(n)
