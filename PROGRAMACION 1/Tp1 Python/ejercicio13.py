"""Pide un número por teclado e indica si es un número primo o no. Un número primo
es aquel solo puede dividirse entre 1 y sí mismo. Por ejemplo: 25 no es primo, ya que
25 es divisible entre 5, sin embargo, 17 si es primo. Un buen truco para calcular la raíz
cuadrada del numero e ir comprobando que si es divisible desde ese número hasta 1.
NOTA: Si se introduce un número menor o igual que 1, directamente es no primo. """
#-----------------------------------------------------------------------------
#Pido al usuario ingresar el número
num = int(input("Ingrese un número para saber si es primo"))
#-----------------------------------------------------------------------------
#Criterio/Condición primo o no primo
divisores = 0
for i in range(1,num + 1):
    if num % i == 0:
        divisores += 1
#-----------------------------------------------------------------------------
#Condición para mostrar resultado (cantidad de divisores)
if divisores == 2:
    print("El número ", num, " es primo")
else:
    print("El número ", num, " NO es primo")