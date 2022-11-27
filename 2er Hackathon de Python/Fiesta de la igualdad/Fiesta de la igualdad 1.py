n = int(input())

lis = list(map(int, input().split(' ')))

print(n * max(lis) - sum(lis))
