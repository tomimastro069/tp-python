
import random

nroRandom = random.randint(0,100)
nroAdivinado = False
cont = 1

while (not nroAdivinado):
    nro = int(input("Adivine el numero"))
    if(nro == nroRandom):
        nroAdivinado = True
    else:
        if(nro > nroRandom):
            print("Es muy alto")
        else:
            print("Es muy bajo")
        cont += 1 

print("Numero encontrado\nCantidad de intentos ", cont)