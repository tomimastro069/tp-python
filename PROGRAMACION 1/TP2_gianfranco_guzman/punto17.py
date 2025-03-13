"""17- Cree una clase FuncionesPrograma y codifique una función estática getFechaString
que reciba como parámetro una fecha y retorne la fecha como una cadena literal.
Ejemplo recibo 15/10/1900, la salida debe ser
Quince de Octubre de mil novecientos.
Cree una clase Principal que contenga un método main y haga uso de la función
getFechaString. """

class FuncionesPrograma:
    #El módulo datetime proporciona clases para manipular fechas y horas
    from datetime import datetime

    now= datetime.now()
    
    #strtime formatea la hora y fecha a formato cadena
    getFechaString = now.strftime("%Y/%m/%d %H:%M:%S") #modifico el formato
    getFechaString= str(getFechaString)
    print(getFechaString)



