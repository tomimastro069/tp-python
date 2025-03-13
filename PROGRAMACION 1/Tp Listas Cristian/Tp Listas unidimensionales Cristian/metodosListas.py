def numeroNatural(solicitud = ""):
    """
    Exige que el valor ingresado sea natural

    Args: 
        solicitud (String): Alguna solicitud en especifico
    
    Return:
        int: El numero natural ingresado
    """
    while True:
        try:
            natural = int(input(solicitud))
            if (natural > 0):
                break
        except ValueError:
            print("Valor incorrecto. Se espera un entero")
    return natural

def numeroEntero(solicitud = ""):
    """
    Exige que el valor ingresado sea entero

    Args: 
        solicitud (String): Alguna solicitud en especifico
    
    Return:
        int: El numero entero ingresado
    """
    while True:
        try:
            entero = int(input(solicitud))
            break
        except ValueError:
            print("Valor incorrecto. Se espera un entero")
    return entero

def llenarLista():
    """
    Devuelve una lista
   
    Return:
        list: La lista ingresada por el usuario
    """
    tamaño = numeroNatural("Ingrese el tamaño: ")
    lista = list()
    for i in range(0,tamaño):
        nro = numeroEntero(f"{i+1} Numero: ")
        lista.append(nro)
    return lista
    