"""4- Desarrolle un programa que ayude a una cajera a determinar el número de billetes y
monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50,
20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de
dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete
de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05
centavos. Plantee el algoritmo planteando métodos para su resolución."""

dinero=float((input(f"Ingrese la cantidad de dinero de la caja: ")))

billetes = [200,100,50,20,10,5,2,1]
for billete in billetes: #"billete" va a ir tomando 1 por 1 los valores de la lista
    if dinero >= billete:
        cant_billetes= int(dinero // billete)
        dinero = round(dinero % billete, 2) #"round" redondea a 2 decimales para envitar errores de punto flotante
        print(f"Cantidad de billetes de {billete}: {cant_billetes}")

monedas= [0.50, 0.25, 0.10, 0.05]
for moneda in monedas: #"moneda" va a ir tomando 1 por 1 los valores de la lista
    if dinero >= moneda:
        cant_monedas= int(dinero // moneda)
        dinero = round(dinero % moneda,2) #"round" redondea a 2 decimales para envitar errores de punto flotante
        print(f"Cantidad de monedas de {moneda}: {cant_monedas}")

#dinero por debajo de la menor cantidad:
if dinero > 0:
    print(f"Resto: {dinero}")