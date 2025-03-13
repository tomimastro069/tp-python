from Matriz import Matriz
from Celda  import Celda
from metodos import numeroPositivoEntero

def main():
    matriz  = Matriz()
    while(True):
        if (ingresarValores(matriz)):
            break
    matriz.mostrarCeldas()           

    
def ingresarValores(matriz):
    valor = input("Ingrese el valor: ")
    if (valor ==  "FIN"):
        return True
    fila = numeroPositivoEntero("Ingrese la fila:")
    columna = numeroPositivoEntero("Ingrese la columna: ")
    matriz.ingresarCeldas(fila,columna,valor)
    return  False


if __name__ == "__main__":
    main()