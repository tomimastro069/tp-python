
def ingresar_numero():
    valorDecimal = float(input("Ingrese un valor decimal: "))
    convertir_a_int(valorDecimal)
    convertir_a_short(valorDecimal)
    convertir_a_long(valorDecimal)
    convertir_a_float(valorDecimal)

def convertir_a_int(valorDecimal):
    print(f"Variable convertida a int {int(valorDecimal)}")

def convertir_a_short(valorDecimal):
    if (-32768 <= valorDecimal <= 32767):
        print("Tu numero en Short es: ", int(valorDecimal))
    else:
        print("Tu numero no se encuentra dentro del rango de 16bits")

    print(f"Variable convertida a short {valorDecimal }")

def convertir_a_long(valorDecimal):
    if (-2^63 >= valorDecimal >= 2^63-1):
            print("Tu numero no se encuentra dentro del rango de 64bits")
    else:
        print("Tu numero en long es: ", int(valorDecimal))


def convertir_a_float(valorDecimal):
    print(f"Variable convertida a float {float(valorDecimal)}")


ingresar_numero()