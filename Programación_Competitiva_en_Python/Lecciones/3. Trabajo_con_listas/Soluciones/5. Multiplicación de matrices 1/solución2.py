a = []
for i in range(2):
        a.append(list(map(int, input().split())))

input()
        
b = []
for i in range(2):
        b.append(list(map(int, input().split())))

for i in range(2):
    for j in range(2):
        x = 0
        for k in range(2):
            x += a[i][k] * b[k][j]
        print(x, end=" ")
    print()