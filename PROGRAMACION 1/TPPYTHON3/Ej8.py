
def encontrar_repetidos(Lista):
    frecuencia={}
    for i in Lista:
        if i in frecuencia:
            frecuencia[i] = frecuencia[i] + 1
        else:
            frecuencia[i] = 1
    repetidos = [i for i, count in frecuencia.items() if count > 1]
    return repetidos

def main():
    cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
    Lista = [None] * cantidaddefilas
    for i in range(len(Lista)):
        Num = int(input(f"Ingrese el número de la casilla {i}: "))
        Lista[i] = Num

    elementos_repetidos = encontrar_repetidos(Lista)
    if elementos_repetidos:
        print("Los elementos que se repiten en la lista son:", elementos_repetidos)
    else:
        print("No hay elementos repetidos en la lista.")

if __name__ == "__main__":
    main()

