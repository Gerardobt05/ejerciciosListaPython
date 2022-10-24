# Ejercicio 5 #
'''
Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y 
posterior ordene los elementos de menor a mayor
'''

import random

#Función que que devuelve una lista con 10 números aleatorios entre 0 y 10
def listaAleatoria():
    lst = []
    for i in range(0,10):
        lst.append(random.randint(0,10))
    return lst

 
#Creamos una función que ordene de menor a mayor
def listaMenoraMayor(lst):
    lst.sort()
    return lst

def ejercicio5():
    lst = listaAleatoria()
    print(listaMenoraMayor(lst))
    
