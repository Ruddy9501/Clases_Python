if __name__ == '__main__':
    
    a = int(input())
    b = int(input())
    n = int(input())
   
    arr = [int(_) for _ in input().split(' ')]
    ultimo = 0
    sol = 0
    for i in range(n):
      
        if arr[i] - ultimo > a:
            ultimo = arr[i-1]
            sol += 1
    
    if b - ultimo > a:
        sol += 1
    
    print(sol)
