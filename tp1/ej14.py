A = 0
import random
B = 0
cont = 1
A = random.randint(0, 100)
while B != A:
    B = int(input("ingrese un numero entre 1 y 100 "))
    cont = cont +1
    if B < A:
        print("El numero es muy bajo")
    elif B > A:
        print("El numero es muy alto")

print("Felicidades has descubierto el numero, te a llevado: ", (cont ) ," intentos")



 