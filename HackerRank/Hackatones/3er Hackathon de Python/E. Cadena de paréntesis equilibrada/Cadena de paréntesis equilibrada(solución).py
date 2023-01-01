def es_equilibada(line):
    solucion = "true"
    stack = []
    for car in line:
        
        if car == '(' or car == '{' or car == '[':
            stack.append(car)
        else:    
    
            if len(stack) == 0:
                solucion = "false"
                break
            
            if (stack[-1] == "(" and car == ")") or (stack[-1] == "{" and car == "}") or (stack[-1] == "[" and car == "]"):
                stack.pop()
            else:
                solucion = "false"
                break   
                
    if len(stack) > 0:
        solucion = "false"
    
    return solucion
    
while True:
    try:
        line = input()
    except EOFError:
        break
        
    print(es_equilibada(line))
