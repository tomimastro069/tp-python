class Fraccion:

    #Constructor
    def __init__(self,num,den) -> None:
        self.num = num
        self.den = den

    #Metodos para resolver las operaciones
    @staticmethod
    def sumarFracciones(f1,f2):
        num = f1.num * f2.den + f2.num * f1.den
        den = f1.den * f2.den
        f3 = Fraccion(num,den)
        return f"{f3.num}/{f3.den}"
    
    @staticmethod
    def restarFracciones(f1,f2):
        num = f1.num * f2.den - f2.num * f1.den
        den = f1.den * f2.den
        f3 = Fraccion(num,den)
        return f"{f3.num}/{f3.den}"

    @staticmethod
    def multiplicarFracciones(f1,f2):
        num = f1.num * f2.num
        den = f1.den * f2.den
        f3 = Fraccion(num,den)
        return f"{f3.num}/{f3.den}"

    @staticmethod
    def dividirFracciones(f1,f2):
        num = f1.num * f2.den
        den = f1.den * f2.num
        f3 = Fraccion(num,den)
        return f"{f3.num}/{f3.den}"
    
    #Metodo toString para darle formato al objeto("Fraccion")
    def __str__(self) -> str:
        return f"toString :{self.num}/{self.den}"

class OperacionesFraccion:
    @staticmethod
    def main():
        
        print("\tPrimera Fraccion:")
        num = int(input("Ingresa el numerador: "))
        den = int(input("Ingresa el denominador: "))
        f1 = Fraccion(num,den)

        print("\n\tSegunda Fraccion:")
        num = int(input("Ingresa el numerador: "))
        den = int(input("Ingresa el denominador: "))
        f2 = Fraccion(num,den)
        

        print(f"Suma: {Fraccion.sumarFracciones(f1,f2)}")
        print(f"Resta: {Fraccion.restarFracciones(f1,f2)}")
        print(f"Multiplicacion: {Fraccion.multiplicarFracciones(f1,f2)}")
        print(f"Division: {Fraccion.dividirFracciones(f1,f2)}")
        
if __name__ == "__main__":
    OperacionesFraccion.main()