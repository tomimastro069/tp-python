def eliminar_duplicados(Lista):
    conjunto =set(Lista)
    Lista_nueva = []
    for i in conjunto:
        Lista_nueva.append(i)
    return Lista_nueva


def main():
    cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
    Lista=[None] * cantidaddefilas
    for i in range(len(Lista)):
        Num=int(input(f"ingrese el Numero de la casilla {i} "))
        Lista[i] = Num
    Lista_nueva = eliminar_duplicados(Lista)
    print("Nueva lista sin duplicados: ", Lista_nueva)
if __name__ == "__main__":
    main()
    

def eliminar_duplicados(Lista):
    conjunto = set(Lista)
    Lista_nueva = []
    for i in conjunto:
        Lista_nueva.append(i)
    return Lista_nueva

