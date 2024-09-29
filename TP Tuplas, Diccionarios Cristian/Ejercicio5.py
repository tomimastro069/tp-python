"""
Ejercicio 5: Contar elementos en una tupla 
Dada la siguiente tupla: 
numeros = (1, 2, 2, 3, 4, 4, 4, 5) 
a) Cuenta cuántas veces aparece el número 4 en la tupla. 
b) Imprime el resultado
"""
numeros = (1, 2, 2, 3, 4, 4, 4, 5) 
veces = 0

for numero in numeros:
    if numero == 4:
        veces +=1
print(f"Tupla Numeros: {numeros}")
print(f"a) Veces que aparece el cuatro: {veces}")