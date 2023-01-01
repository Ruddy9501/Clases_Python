w = int(input())

es_posible = False
for x in range(1, w):
    for y in range(1, w):
        if x%2==0 and y%2==0 and x+y==w:
            es_posible = True

if es_posible == True:
    print('YES')
else:
    print('NO')
