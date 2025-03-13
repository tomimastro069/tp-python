def numeroPositivoEntero(solicitud=""):
    while True:
        try:
            n = int(input(solicitud))
            if n > 0:
                return n
        except ValueError:
            print("El valor ingresado no es un número entero")

def numeroPositivoFlotante(solicitud = ""):
    while True:
        try:
            n = float(input(solicitud))
            if n > 0:
                return n
            else:
                print("El número debe ser positivo")
        except ValueError:
            print("El valor ingresado no es un número")
            
        