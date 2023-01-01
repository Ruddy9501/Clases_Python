n = int(input())
 
while (len(set(list(str(n + 1)))) != len(list(str(n + 1)))):
       n += 1
       
print(n+1)
