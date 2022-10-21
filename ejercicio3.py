# Ejercicio 3 #
'''
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor
'''
# Ejercicio 3 #
'''
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor
'''
#Notas alumno

def obtenerNotas(n):
    totalNotas = 0
    lstNotas = []
    while(totalNotas < n):
        try:
            nota = float(input("Dime la nota: "))
            if(nota <= 10):
                lstNotas.append(nota)
                totalNotas += 1
            else:
                print("La nota ", nota , " no es correcta. ")
        except:
            print("Tiene que ser un número")
    return lstNotas

#calculamos la nota media

def notaMedia(lst):
    resul = sum(lst) / len(lst)
    return resul

#calculamos la nota más baja

def notaMasBaja(lst):
    return min(lst)

#calculamos la nota más alta

def notaMasAlta(lst):
    return max(lst)


#Calculamos el ejercicio

def ejercicio3():
    listado = obtenerNotas(5)
    
    print("Las notas son: ", listado) 
    print("La nota media es: ", notaMedia(listado)) 
    print("La nota más alta es: ", notaMasAlta(listado)) 
    print("La nota más baja es: ", notaMasBaja(listado))
