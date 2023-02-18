def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input())
fact = factorial(n)

while fact % 10 == 0:
    fact //= 10
    
print(fact % 10)