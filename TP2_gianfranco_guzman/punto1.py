"""1- CASTEO: Codifique un programa que solicite el ingreso de un numero decimal y
asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para
convertir la variable a los siguientes tipos de datos, short, int, long, float investigue las
diferentes formas de lograr la conversión. Muestre por pantalla el resultado de las
conversiones. """
num= input("Ingrese un numero decimal: ")

#estructura try - except, se utiliza para manejar excepciones y errores controlados. permite que se siga eyecutando el codigo 
# sin interrumpirse abruptamente debido a un error
try:
    valor_decimal= float(num)
    valor_entero= int(valor_decimal)

    print(f"numero ingresado a decimal: {valor_decimal}")
    print(f"numero ingresado a entero / long: {valor_entero}")

    #importamos modulo struct, se utiliza para trabajar con datos binarios 
    import struct

    num= int(valor_decimal)
    
    #para convertir el numero a short debo verificar si esta dentro del rango de 16 bits
    if -32768 <= valor_entero <= 32767:
    
    #convertir a entero de 16 bits 
        valor_bytes= struct.pack("h", valor_entero)
        valor_short = struct.unpack("h", valor_bytes)[0]
        print(f"valor ingresado a bytes: {valor_bytes}")
        print(f"el valor ingresado esta en rango short: {valor_short}")
    else:
        print(f"El número ingresado está fuera del rango de un short (entero de 16 bits).")

except ValueError:
    print(f"El valor ingresado no es un número de punto flotante válido.")