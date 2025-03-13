"""Codifique un programa de consola en Python que permita realizar las siguientes
acciones:
Generar un número aleatorio entre 0 y 100, para ello use la siguiente función:
random.randint(0, 100)
Una vez generado el número codifique la lógica necesaria para encontrar el número
aleatorio ayudando al usuario informando al mismo si el número ingresado es mayor o
menor al número aleatorio buscado. Una vez encontrado el número muestre la
cantidad de intentos necesarios para lograrlo."""
#-------------------------------------------------------------------
#Genero un número aleatorio
from random import *
resultado = randint(0,100)
#-------------------------------------------------------------------
#Intentos fallidos
numIngresado = int(input("Ingrese un número"))
intentos = 1
while numIngresado != resultado:
    if numIngresado > resultado:
        print("Es muy alto")
        intentos += 1
        numIngresado = int(input("Ingrese un número"))
    elif numIngresado < resultado:
        print("Es muy bajo")
        intentos += 1
        numIngresado = int(input("Ingrese un número"))
#-------------------------------------------------------------------
#Acertar el número
if numIngresado == resultado:
    print("Correcto, número encontrado. Cantidad de intentos: ", intentos)

