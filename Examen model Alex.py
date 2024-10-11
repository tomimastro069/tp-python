import random  # Importa la biblioteca random para generar números aleatorios

# Función para ingresar datos y validar que sean enteros
def ingresar_datos(cadena):
    while True:
        try:
            dato = int(input(cadena))  # Intenta convertir el dato ingresado a entero
            return dato  # Si es un entero válido, lo devuelve
        except ValueError:  # Si ocurre un error de conversión, captura la excepción
            print("Error, ingrese un dato valido.")  # Muestra un mensaje de error

def main():
    # Bucle para ingresar la cantidad de filas, asegurando que sea >= 3
    while True:
        cantidad_filas = ingresar_datos("Ingrese la cantidad de filas: ")
        if (cantidad_filas < 3):
            print("El numero de filas debe ser mayor o igual a 3.")
        else:
            break 
    
    # Bucle para ingresar la cantidad de columnas, asegurando que sea >= 2
    while True:
        cantidad_columnas = ingresar_datos("Ingrese la cantidad de columnas: ")
        if (cantidad_columnas < 2):
            print("El numero de columnas debe ser mayor o igual a 2.")
        else:
            break 
    
    # Bucle para decidir si la carga de datos será manual o automática
    while True:
        random_booleano = ingresar_datos("Desea que la carga de datos sea manual?\n1-si\n2-no\n")
        if not (random_booleano == 1 or random_booleano == 2):
            print("Ingrese un '1' o un '2'.")  # Validación para asegurarse de que el usuario ingrese 1 o 2
        else:
            break  

    matriz_original = []  # Inicializa la lista que contendrá la matriz original

    # Carga manual de los datos en la matriz
    if (random_booleano == 1):
        for i in range(cantidad_filas):
            fila_elementos = []  # Lista que almacena los elementos de la fila actual
            for j in range(cantidad_columnas):
                while True:
                    # Solicita el valor de cada elemento y asegura que esté en el rango de 1 a 999
                    valor_elemento = ingresar_datos(f"Ingrese el valor de el elemento ({i} , {j}): ")
                    if (valor_elemento < 1 or valor_elemento > 999):
                        print("Ingrese un numero entre 1 y 999")
                    else:
                        fila_elementos.append(valor_elemento)  # Agrega el elemento a la fila
                        break
            matriz_original.append(fila_elementos)  # Agrega la fila a la matriz
    else:
        # Carga automática de datos en la matriz usando números aleatorios
        for i in range(cantidad_filas):
            fila_elementos = []
            for j in range(cantidad_columnas):
                valor_elemento = random.randint(1,999)  # Genera un número aleatorio entre 1 y 999
                fila_elementos.append(valor_elemento)
            matriz_original.append(fila_elementos)

    # Imprime la matriz original
    print("Matriz Original: ")
    for i in matriz_original:
        print(i)

    matriz_sumatoria = []

    # Suma los valores de cada fila y los almacena en 'matriz_sumatoria'
    for i in range(cantidad_filas):
        valor_fila = 0
        for j in range(cantidad_columnas):
            valor_fila += matriz_original[i][j]  # Suma los elementos de la fila
        matriz_sumatoria.append(valor_fila)  # Guarda la suma total de la fila

    # Imprime la matriz sumatoria
    print("Matriz sumatoria:")
    for i in matriz_sumatoria:
        print(i)

    # Inicializa una lista para almacenar la sumatoria y el índice de cada fila
    matriz_sumatoria_ordenada = []

    # Crea una lista de pares (suma de la fila, índice de la fila)
    for i in range(cantidad_filas):
        indice = []
        indice.append(matriz_sumatoria[i])  # Almacena la suma de la fila
        indice.append(i)  # Almacena el índice de la fila
        matriz_sumatoria_ordenada.append(indice)

    # Bucle para ordenar la matriz sumatoria de mayor a menor usando el método de burbuja
    booleano = False
    while not booleano:
        booleano = True  # Supone que la lista está ordenada
        for i in range(len(matriz_sumatoria_ordenada)-1):
            if matriz_sumatoria_ordenada[i][0] < matriz_sumatoria_ordenada[i+1][0]:
                # Intercambia los elementos si están en el orden incorrecto
                aux = matriz_sumatoria_ordenada[i]
                matriz_sumatoria_ordenada[i] = matriz_sumatoria_ordenada[i+1]
                matriz_sumatoria_ordenada[i+1] = aux
                booleano = False  # Indica que hubo un intercambio y necesita seguir ordenando

    # Imprime la matriz sumatoria ordenada con sus respectivos índices
    print("Matriz sumatoria ordenada con indices: ")
    for i in matriz_sumatoria_ordenada:
        print(i)

    # Calcula la suma total de todos los valores de la matriz sumatoria
    sumatoria_elementos = 0
    for i in range(cantidad_filas):
        sumatoria_elementos += matriz_sumatoria_ordenada[i][0]  # Suma los valores de la columna de sumatorias

    # Imprime la suma total de los valores de la columna sumatoria
    print(f"Sumatoria de la columna de matriz sumatoria: {sumatoria_elementos}")

# Ejecuta el programa si es ejecutado directamente (no importado)
if __name__ == "__main__":
    main()
