def main():
    cadena = input("Ingrese una cadena: ")
    print("Hay digitos en la cadena" if contieneNumeros(cadena) else "No hay digitos en la cadena") #Operador ternario

def contieneNumeros(cadena):
    for i in cadena:
        if i.isdigit(): #Revisa si en la posicion i se encuentra un digito
            return True
    return False

if __name__ == "__main__":
    main()