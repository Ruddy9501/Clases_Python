def f(n):
    
    numero = n
    suma = 0
    while numero > 0:
        digito = numero % 10
        numero = numero // 10
        
        suma = suma + digito**3
   
    return n == suma


if __name__ == '__main__':
    
    n = int(input())
    numero1 = n
    
    while f(numero1) == False:
        numero1 = numero1 - 1
        
    numero2 = n
    while f(numero2) == False and numero2 - n <= n - numero1:
        numero2 = numero2 + 1
    
    if numero2 - n < n - numero1:
        print(numero2)
    else:
        print(numero1)
