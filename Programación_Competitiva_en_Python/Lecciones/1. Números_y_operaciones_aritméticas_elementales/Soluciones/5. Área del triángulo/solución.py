a, b, c = list(map(int, input().split(' ')))

Sp = (a+b+c)/2
A = (Sp*(Sp-a)*(Sp-b)*(Sp-c))**(1/2)

print(int(A))