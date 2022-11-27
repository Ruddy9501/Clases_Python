fibonacci = [0] * 105
fibonacci[1] = 1
fibonacci[2] = 1

for i in range(3, 101):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    
n = int(input())

print(fibonacci[n])