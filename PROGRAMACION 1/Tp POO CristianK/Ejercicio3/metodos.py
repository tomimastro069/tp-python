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
            
def esBebida(var):
    var = str(var).lower()
    if(var == "true"):
        return True
    elif (var == "false"):
        return False
    else:
        while(True):
            print("La respuesta debe ser True o False")
            var = input("¿Es una bebida? (True/False): ")
            return esBebida(var)