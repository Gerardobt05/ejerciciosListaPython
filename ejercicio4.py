# Ejercicio 4 #
'''
Programa que declare una lista y la vaya llenando de números hasta que introducimos un número negativo.
Entonces se debe imprmir el vector (sólo los elementos introducidos)
'''

#Creamos una lista
def listanumeros():
    lst = []
    noFin = True
    while(noFin):
        try:
            cadena = input("Dime un número: ")
            print(cadena)
            num = int(cadena)
            if(num<0):
                noFin = False
            else:
                lst.append(num)
        except:
            print("Tiene que ser un número")
    return lst
    
