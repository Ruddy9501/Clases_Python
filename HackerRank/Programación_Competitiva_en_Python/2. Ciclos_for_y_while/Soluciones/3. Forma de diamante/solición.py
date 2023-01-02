n = int(input())

mid = (n+1)//2
for i in range(1, n+1):
    for j in range(1, n+1):
        d = abs(i-mid) + abs(j-mid)
        d2 = min(i-1, n-i) + min(j-1, n-j)
        if d < (n+1)/2:
            print('*', end='')
        else:
            print(' ', end='')
        
        if j != n:
            print(' ', end='')
    print()