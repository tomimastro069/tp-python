"""15- Indique que sucede si realizo la siguiente declaración de variable:
x = None print(x)
Explique y ejemplifique el uso de None"""

#El None es un objeto especial que representa la ausencia de de un valor:

#*En funciones, None se utiliza a menudo como valor por defecto para parámetros opcionales.
#*En estructuras de datos como listas, diccionarios y tuplas, None se puede usar para indicar 
#que un elemento no tiene un valor asignado.
#*Algunas funciones pueden devolver None para indicar que no hay un resultado válido.

#Ejemplo de valor None:
x= None 
print(x) #salida por pantalla "None"

lista=[1,None,3]
print(lista) #salida por pantalla " [1, None, 3]

def buscar_elemento (lista, elemento):
    for i in lista:
        if i == elemento:
            return i
    return None

resultado = buscar_elemento([1,None,3], 2)
print([resultado]) #Al no tener elemento "2", por pantalla sale "[None]"
