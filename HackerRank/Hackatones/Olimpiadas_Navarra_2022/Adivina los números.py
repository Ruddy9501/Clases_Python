if __name__ == '__main__':
    
    a = []
    for _ in range(7):
        a.append(int(input()))

    a.sort ()
    
    print(a[0],end= " ")
    print(a[1],end= " ")
    print(a[6]-a[0]-a[1])
