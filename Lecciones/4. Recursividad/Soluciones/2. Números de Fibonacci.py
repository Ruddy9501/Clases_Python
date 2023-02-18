fib = [-1] * 101

def fibonacci(n):
    if n <= 2:
        return 1
    
    if fib[n] != -1:
        return fib[n]
    
    fib[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib[n] 

n = int(input())
fib = fibonacci(n)
print(fib)