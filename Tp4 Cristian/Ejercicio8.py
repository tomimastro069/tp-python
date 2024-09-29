"""
Ejercicio 8: Eliminar elementos de un diccionario 
Dado el diccionario: 
mascota = {"nombre": "Firulais", "especie": "Perro", "edad": 5} 
a) Elimina la clave edad del diccionario. 
b) Imprime el diccionario después de eliminar esa clave
"""
mascota = {"nombre": "Firulais", "especie": "Perro", "edad": 5} 
print(f"Diccionario: {mascota}")

mascota.pop("edad")

print(f"Edad eliminada\n{mascota}")