def f(n):
    
    d = []
    while n > 0:
        d.append(n%10)
        n //= 10
    
    if len(d) == len(set(d)):
        return True
    else:
        return False
    

n = int(input())

while (f(n + 1) == False):
       n += 1
       
print(n+1)