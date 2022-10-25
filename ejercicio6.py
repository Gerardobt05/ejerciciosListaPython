# Ejercicio 6 #
'''
Crea un programa que pida un número al usuario, un número de mes ( por ejemplo, el 4). 
El programa dirá cuántos días tiene (por ejemplo 30) y el nombre del mes. Debes usar listas. Nota: En una lista podemos guardar listas.
Para simplificarlo vamos a suponer que febrero tiene 28 días
'''
def pedirmes():
    lstMes = [["Enero" , 31],["Febrero" , 28],["Marzo" , 31],["Abril" , 30],["Mayo" , 31],["Junio" , 30],["Julio" , 31],["Agosto" , 31],["Septiembre" , 30],["Octubre" , 31],["Noviembre" , 30],["Diciembre" , 31]]
    try:
        numMes = int(input("Dime un número del 1 al 12: "))
        if(numMes > 12 or numMes < 1):
            print("Ese número no vale")
        else:
            print(lstMes[numMes-1][0], " tiene ", lstMes[numMes-1][1], " días.")
        
            
    except:
        print("Tiene que ser un número")
