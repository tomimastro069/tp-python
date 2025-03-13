import random
fil, col = 0, 0
listaCol = list()
listaColOrdenada = list()

def main():
    while True:
        opcion = verificarEnteroFloat("Como desea generar la lista\n1_Manual\n2_Aleatoria\n", "")
        if opcion not in (1, 2):
            print("Error, Debe ingresar 1-2")
        else:
            match opcion:
                case 1: 
                    lista = llenarListaManual()
                case 2: 
                    lista = llenarListaAutomatica()
            break
    print("Punto 1: \n", lista, "\n")

    print("Punto 2: \n")
    mostrarLista(lista)

    print("Punto 3 y 4: \n")
    listaColumna(lista)

    print("Punto 5 y 6")
    lista_dos_columnas = funcionPuntoCinco()
    mostrarLista(lista_dos_columnas)

    print("\nPunto 7\n")
    punto7 = funcionPuntoSiete()
    print("Suma: ", punto7)

def funcionPuntoSiete():
    suma = 0
    for i in range(len(listaCol)):
        suma += listaCol[i]
    return suma

def ordenamientoMm(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]:  # Cambio para ordenar de mayor a menor
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def indiceOriginal(valor):
    for i in range(len(listaCol)):
        if listaCol[i] == valor:
            return i
    return -1  # Si no se encuentra el valor, se devuelve -1

def funcionPuntoCinco():
    listaColOrdenada = ordenamientoMm(listaCol.copy())  # Ordenar de mayor a menor
    listaDosColumnas = [[0 for _ in range(2)] for _ in range(fil)]
    for i in range(fil):
        listaDosColumnas[i][0] = listaColOrdenada[i]
        indice_original = indiceOriginal(listaColOrdenada[i])
        listaDosColumnas[i][1] = int(indice_original)
    return listaDosColumnas

def listaColumna(lista):
    global fil, col
    fil, col = len(lista), len(lista[0])
    listaCol.clear()
    for i in range(fil):
        suma = 0
        for j in range(col):
            suma += lista[i][j]
        listaCol.append(suma)
    for i in listaCol:
        print(i)

def mostrarLista(lista):
    fila = ""
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            fila += f"{lista[i][j]:.2f}  "  # Formatear a dos decimales máximo
        print(fila)
        fila = ""

def llenarListaAutomatica():
    fil, col = definirFilCol()
    lista = [[round(random.uniform(1, 999), 2) for _ in range(col)] for _ in range(fil)]
    return lista

def definirFilCol():
    while True:
        fila = verificarEnteroFloat("Ingrese las filas: ", "")
        columna = verificarEnteroFloat("Ingrese las columnas: ", "")
        if valorMinimoLista(fila, columna):
            break
    return fila, columna

def llenarListaManual():
    fil, col = definirFilCol()
    lista = [[0 for _ in range(col)] for _ in range(fil)]
    for i in range(fil):
        for j in range(col):
            lista[i][j] = verificarEnteroFloat(descripcion=f"\nIngrese el numero [{i}][{j}]: ", condicion="lista")
    return lista

def verificarEnteroFloat(descripcion, condicion):
    while True:
        try:
            if condicion == "lista":
                num = float(input(descripcion))
            else:
                num = int(input(descripcion))
            if 1 <= num <= 999:
                return num
            else:
                print("Error: El valor debe estar entre 1 y 999.")
        except ValueError:
            print("Valor invalido.")

def valorMinimoLista(fil, col):
    return fil >= 3 and col >= 2

if __name__ == "__main__":
    main()