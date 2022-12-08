n = int(input())

fact = 1
for j in range(2, n+1):
    fact = fact * j

    while fact % 10 == 0:
        fact //= 10
        
print(fact%10)
