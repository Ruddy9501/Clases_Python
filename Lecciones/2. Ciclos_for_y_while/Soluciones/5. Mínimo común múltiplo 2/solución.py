def gcd(a, b):
    
    while a > 0:
        b = b % a
        a, b = b, a
    
    return b

a, b = list(map(int, input().split()))
print(a*b//gcd(a, b))