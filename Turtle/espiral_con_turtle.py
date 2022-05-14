# Importamos todas las funciones de la biblioteca turtle
from turtle import *

# pintamos el color de fondo de negro
#bgcolor('black')
# Aumentamos el grosor de la tortuga utilizado para pintar 
width(2)
# Aumentamos la velocidad de la animación de la tortuga
speed(10)

def espiral():
    # Creamos un arreglo con los valores de los colores que empezará la tortuga
    colores = ['blue', 'pink', 'cyan']
    # Creamos la variable contadora y la inicializamos con valor cero 
    contador = 0
    # El ciclo se repite mientras el valor del contador sea menor que 300 
    while contador < 300:
        # Elegimos un nuevo color para que la tortuga dibuje
        pencolor(colores[contador % 3])
        # Movemos la tortuga hacia adelante la distancia indicada
        forward(contador*4)
        # La tortuga gira 121 grados a la derecha 
        right(121)
        # Se incrementa en uno el valor del contador
        contador = contador + 1

# Llamamos a la función encargada de dibujar la espiral 
espiral()
