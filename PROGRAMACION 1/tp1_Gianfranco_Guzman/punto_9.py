#9) Muestra los números del 1 al 100 (ambos incluidos) divisibles entre 2 y 3. Utiliza el
#bucle que desees
cont= 1
for cont in range(1,101):
    if((cont % 2 == 0)and(cont % 3 == 0)):
        print(cont)
cont= cont + 1