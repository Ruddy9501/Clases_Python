n, m = list(map(int, input().split()))

tot = 0
for i in range(n):
    su = sum(list(map(int, input().split())))
    tot += su
    
print(int(tot / (n*m) + 0.5))