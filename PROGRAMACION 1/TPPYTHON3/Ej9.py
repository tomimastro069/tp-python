def es_primo(num):
    
    if num == 1:
        return True
    if num < 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
    
def lista_numeros_primos(Lista):
    lista_numeros_primos = []
    for i in Lista:
        if es_primo(i):
            lista_numeros_primos.append(i)
    return lista_numeros_primos

def main():
    cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
    Lista = [None] * cantidaddefilas
    for i in range(len(Lista)):
        Num = int(input(f"Ingrese el número de la casilla {i}: "))
        Lista[i] = Num

    primos = lista_numeros_primos(Lista)
    print("Los números primos en la lista son:", primos)

if __name__ == "__main__":
    main()