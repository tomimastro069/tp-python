"""Cree una clase Fracción con dos atributos, numerador y denominador.
Agregue a la clase los siguientes 4 métodos e implemente los mismos:
sumarFracciones(Fraccion f1, Fraccion f2)
restarFracciones(Fraccion f1, Fraccion f2)
multiplicarFracciones(Fraccion f1, Fraccion f2)
dividirFracciones(Fraccion f1, Fraccion f2)
Todos los métodos deben retornar la fracción resultante de la operación.
Cree una clase OperacionesFraccion que contenga un método main donde se solicite
al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos
Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos
implementados anteriormente asignando el resultado a una nueva variable de tipo
Fracción y mostrando por pantalla el resultado de las operaciones realizadas"""

from math import gcd #Importo la funcion para calcular el minimo comun divisor

class Fracción:
    def __init__(self,numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador= numerador
        self.denominador= denominador
        self.simplificar()

    def simplificar(self):
        mcd = gcd(self.numerador, self.denominador) #"gsd" calcula el maximo comun divisor
        self.numerador //= mcd # //= realiza una division entera
        self.denominador //= mcd
    
    def __str__(self): #representacion en cadena
        return f"{self.numerador}/{self.denominador}"
    
    @staticmethod #metodo estatico
    def Sumar_Fracciones(f1,f2):
        num= f1.numerador * f2.denominador + f2.numerador * f1.denominador
        den= f1.denominador * f2.denominador
        return Fracción(num, den)
    
    @staticmethod
    def Restar_Fracciones(f1,f2):
        num= f1.numerador * f2.denominador - f2.numerador * f1.denominador
        den= f1.denominador * f2.denominador
        return Fracción(num, den)

    @staticmethod
    def Multiplicar_Fracciones(f1,f2):
        num= f1.numerador * f2.numerador
        den= f1.denominador * f2.denominador
        return Fracción(num, den)
    
    @staticmethod
    def Dividir_Fracciones(f1,f2):
        num= f1.numerador * f2.denominador
        den= f1.denominador * f2.numerador
        return Fracción(num, den)

class Operaciones_Fracción:
    @staticmethod
    def main ():
        print("Ingrese los valores para la primera fracción:")
        num1 = int(input("Numerador 1: "))
        den1 = int(input("Denominador 1: "))

        print("Ingrese los valores para la segunda fracción:")
        num2 = int(input("Numerador 2: "))
        den2 = int(input("Denominador 2: "))

        f1= Fracción(num1, den1)
        f2= Fracción(num2, den2)

        suma= Fracción.Sumar_Fracciones(f1,f2)
        resta= Fracción.Restar_Fracciones(f1,f2)
        multiplicacion= Fracción.Multiplicar_Fracciones(f1,f2)
        division= Fracción.Dividir_Fracciones(f1,f2)
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")

Operaciones_Fracción.main()
    