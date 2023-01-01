n = int(input())

ss = 0
while n > 0:
    ss += n%10
    n //= 10
    
print(ss)