def minimo_comun_multiplo(a, b):
    if a % b == 0:
        return  b
    return minimo_comun_multiplo(b, a%b)

a, b = list(map(int, input().split()))
gcd = minimo_comun_multiplo(a, b)
mcm = (a * b) // gcd

print(mcm)