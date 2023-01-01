import itertools

def f(tiempos, permutation, n):
    return sum([tiempos[i][permutation[i]] for i in range(n)])

if __name__ == '__main__':
    n = int(input())
    permutations = list(itertools.permutations(range(n)))
    
    tiempos = []
    for _ in range (n):
        tiempos.append([int(_) for _ in input().split(' ')])

    
    mejor_permutacion = permutations[0]
    mejor_tiempo = f(tiempos, permutations[0], n)
    for permutation in permutations:
        nuevo_tiempo = f(tiempos, permutation, n)
        if nuevo_tiempo < mejor_tiempo:
            mejor_tiempo = nuevo_tiempo
            mejor_permutacion = permutation
    
    print (mejor_tiempo)
    for numero_tarea in mejor_permutacion:
        print(numero_tarea+1, end=" ")
