from fractions import Fraction

class Fraccion:
    def __init__(self, numerador, denominador):

        if denominador == 0:

            raise ValueError("El denominador no puede ser cero.")
        
        self.fraccion = Fraction(numerador, denominador)
    
    def sumarFracciones(self, otra):

        resultado = self.fraccion + otra.fraccion

        return Fraccion(resultado.numerator, resultado.denominator)
    
    def restarFracciones(self, otra):

        resultado = self.fraccion - otra.fraccion

        return Fraccion(resultado.numerator, resultado.denominator)
    
    def multiplicarFracciones(self, otra):

        resultado = self.fraccion * otra.fraccion

        return Fraccion(resultado.numerator, resultado.denominator)
    
    def dividirFracciones(self, otra):

        resultado = self.fraccion / otra.fraccion

        return Fraccion(resultado.numerator, resultado.denominator)

    def __str__(self):

        return f"{self.fraccion.numerator}/{self.fraccion.denominator}"


class OperacionesFraccion:

    @staticmethod
    
    def main():
        try:
            num1 = int(input("Ingresa el numerador de la fracción 1: "))

            den1 = int(input("Ingresa el denominador de la fracción 1: "))

            num2 = int(input("Ingresa el numerador de la fracción 2: "))

            den2 = int(input("Ingresa el denominador de la fracción 2: "))
            
            f1 = Fraccion(num1, den1)

            f2 = Fraccion(num2, den2)
            
            suma = f1.sumarFracciones(f2)
            
            resta = f1.restarFracciones(f2)

            multiplicacion = f1.multiplicarFracciones(f2)
            
            division = f1.dividirFracciones(f2)
            
            print(f"Suma: {suma}")
            
            print(f"Resta: {resta}")
            
            print(f"Multiplicación: {multiplicacion}")
            
            print(f"División: {division}")
        
        except ValueError as e:
            
            print(f"Error: {e}")

if __name__ == "__main__":
    OperacionesFraccion.main()
