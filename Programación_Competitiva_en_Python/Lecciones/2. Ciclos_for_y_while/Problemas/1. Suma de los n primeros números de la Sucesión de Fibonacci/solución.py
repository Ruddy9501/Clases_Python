n = int(input())

fibonacci = [0] * 51
fibonacci[1] = fibonacci[2] = 1
for i in range(3, 51):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

print(sum(fibonacci[1:n+1]))