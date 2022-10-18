# Ejercicio 1 #
'''
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y
posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
'''
import random

#Función que que devuelve una lista con 10 números aleatorios entre 0 y 10
def generarListaAleatoria():
    lst = []
    for i in range(0,10):
        lst.append(random.randint(0,10))
    return lst

#Función que calcula el cuadrado de un número
def cuadrado(x):
    return x * x

#Es una función que calcula el cubo de un número
def cubo(x):
    return x * x * x

def ejercicio1():
    lista = generarListaAleatoria()
    
    for i in lista:
        print(i, "cuadrado", cuadrado(i), "cubo", cubo(i))
