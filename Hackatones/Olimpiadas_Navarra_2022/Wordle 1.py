if __name__ == '__main__':
    
    palabra = input()
    n = int(input())
    for i in range(n):
        nueva_palabra = input()
        
        arr1 = []
        arr2 = []
        for j in range(5):
            if palabra[j] != nueva_palabra[j]:
                arr1.append(palabra[j])
                arr2.append(nueva_palabra[j])
       
        arr1.sort()
        arr2.sort()
        
        print(5 - len(arr1), len(set(arr1) & set(arr2))) 
