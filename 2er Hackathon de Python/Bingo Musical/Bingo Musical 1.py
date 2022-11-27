n = int(input())

sol1 = set(list(range(1, 10001)))
sol2 = set()

for i in range(n):
    
    lis = list(map(int, input().split(' ')))[1:]

    
    sol1 = sol1 & set(lis)
    sol2 = sol2 | set(lis)
  
for x in sol1:
    print(x, end = ' ')
print()
for x in sol2:
    print(x, end = ' ')
print()
