# Ejercicio 2
'''
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
'''
def pedirCadenasCaracteres(n):
    lst = []
    for i in range(0, n):
        cadena = input("Dime una palabra: ")
        lst.append(cadena)
    return lst

lst = pedirCadenasCaracteres(5)
lst2 = lst.copy()
lst2.reverse()
print("lst", lst)
print("lst2", lst2)
