"""
 Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100  - 999) 
y  por  medio  del  uso  de  las  operaciones  matemáticas  módulo  10  y  división  por  10 
efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo 
14. Plantee el algoritmo planteando métodos para su resolución.
"""

def main():
    nro = int(input("Ingrese un numero de 3 digitos: "))
    if (100 > nro or nro > 999):
        print("Fuera de rango")
        nro = int(input("Ingrese un numero de 3 digitos: "))
    print(sumar3Digitos(nro))


def sumar3Digitos(nro):
    unidad = nro%10         #Calculo la unidad dividiendo por 10 asignado el resto a unidad
    nro = int(nro/10)       #Divido el nro por 10 para eliminar la unidad
    decena = int(nro%10)    #Calculo la Decena dividiendo por 10 asignado el resto a centena
    nro = int(nro/10)       #Divido el nro por 10 para eliminar la centena
    centena = int(nro%10)   #Calculo la Centena con el resto de dividir por 10 nro
    return unidad + decena + centena

if __name__ == "__main__":
    main()