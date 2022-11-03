import random
# Ejercicio 8 #
'''
Denifinir una estructura de datos con listas que permita guardar la temperatura mínima y máxima de 5 días. 
Realiza un programa que de la siguiente información:
     - La temperatura media de cada día
     - Los días con menos temperatura
     - Que permita leer una temperatura por teclado y muestre los días cuya temperatura máxima coincida con ella, en caso contrario mostrar un mensaje diciendo que no existe ningún día
     
'''

def listaTemperatura(n):
    lst = []
    for i in range(0, n):
        min_ = random.randint(-30, 10)
        max_ = random.randint(10, 40)
        lst.append([min_, max_])
    return lst

def temperaturaMedia(lista):
    lst_media_temp = []
    for i in lista:
        media = (i[0] + i[1]) /2
        lst_media_temp.append(media)
        
        
    return lst_media_temp


def menosTemperatura(lista):
    lista_minimos = []
    temperatura_minima = lista[0][0]
    for i in lista:
        if(i[0] <= temperatura_minima):
            temperatura_minima = i[0]
    print(temperatura_minima)
    
    for i in range(0,len(lista)):
        if(temperatura_minima == lista[i][0]):
           lista_minimos.append(i+1) 
    
    return lista_minimos



lista1 = listaTemperatura(5)
lista2 = listaTemperatura(10)
lista3 = listaTemperatura(0)
