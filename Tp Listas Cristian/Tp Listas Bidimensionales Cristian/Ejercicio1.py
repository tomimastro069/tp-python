"""
Ejercicio 1: Crear una Matriz de Números 
Crea una función que reciba dos parámetros: el número de filas y columnas. La función 
debe  generar  una  matriz  de  ese  tamaño,  donde  los  valores  son  números  enteros 
consecutivos empezando desde 1
"""
import numpy

def crearMatriz(filas,columnas):
    array_consecutivo = numpy.arange(1, filas * columnas + 1) #Crea un array de 1D desde 1 hasta (filas * columnas)
    matriz = array_consecutivo.reshape(filas, columnas) #Cambia la forma de un array sin cambiar sus datos.
    return matriz

def main():
    filas = int(input("Ingrese el numero de filas: "))
    columnas = int(input("Ingrese el numero de columnas: "))
    print(f"Matriz creada: \n{crearMatriz(filas,columnas)}")
    
    

if __name__ == "__main__":
    main()