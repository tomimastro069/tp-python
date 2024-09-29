"""
Ejercicio 4: Verificar existencia de un elemento 
Dada la tupla: 
colores = ("rojo", "verde", "azul", "amarillo") 
a) Verifica si el color "morado" está presente en la tupla.
b) Verifica si el color "azul" está presente en la tupla. 
c) Imprime el resultado de ambas verificaciones.
"""

colores = ("rojo", "verde", "azul", "amarillo") 
print(f"Tupla colores : {colores}")

print(f"a) \"morado\" esta en la tupla" if "morado" in colores else "a) \"morado\" no esta")
print(f"a) \"azul\" esta en la tupla" if "azul" in colores else "a) \"azul\" no esta")
