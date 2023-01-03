n, m = list(map(int, input().split()))
ma = -1
x = 0
y = 0
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(m):
        if a[i][j] > ma:
            ma = a[i][j]
            x = i
            y = j

print(x, y)