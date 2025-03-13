def main():
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    if(sonIguales(palabra1,palabra2)):
        print("Son iguales")
    else:
        print("No son iguales")


def sonIguales(p1,p2):
    return p1 == p2

if __name__ == "__main__":
    main()