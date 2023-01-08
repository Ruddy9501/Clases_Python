n, m= list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        if i == j:
            print("1 ", end="")
        else: 
            print("0 ", end="")
    print()