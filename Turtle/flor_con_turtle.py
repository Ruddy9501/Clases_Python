# Importamos todas las funciones de la biblioteca turtle
from turtle import *

# Creamos un arreglo con los valores de los colores que empeará la tortuga
colores = ['purple', 'red', 'blue', 'yellow', 'orange']

# Implementamos la función que se encarga de dibujar la flor
def flor():
    # Hacemos que la velocidad de la tortuga sea la mayor
    speed(0)
    # Creamos la variable contador y la inicializamos con valor cero 
    contador = 0
    # El ciclo se repite mientras el valor del contador sea menor que 300 
    while contador < 300:
        # Elegimos un nuevo color para que la tortuga dibuje
        color(colores[contador % 5])
        # La tortuga dibuja un círculo pasándole el radio y el ángulo de extensión
        circle(190-contador, 90)
        # La tortuga gira 90 grados a la izquierda
        left(90)
        # La tortuga dibuja un círculo pasándole el radio y el ángulo de extensión
        circle(190-contador, 90)
        # La tortuga gira 18 grados a la izquierda
        left(18)
        # Se incrementa en uno el valor del contador
        contador = contador + 1
        
# Llamamos a la función encargada de dibujar la flor      
flor()
