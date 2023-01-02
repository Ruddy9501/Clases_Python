a = list(map(int, input().split()))
for i in range(a[0], a[1]+1):
    sdiv = 0
    for j in range(1, i):
        if i%j == 0:
            sdiv += j
    
    if sdiv == i:
        print(i, end=' ')