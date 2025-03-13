class OperacionMatematica:
    #Constructor
    def __init__(self,n1,n2) -> None:
        self.n1 = n1
        self.n2 = n2

    #Funciones para hacer las operaciones
    def sumarNumeros(self):
        return self.n1 + self.n2

    def restarNumeros(self):
        return self.n1 - self.n2

    def multiplicarNumeros(self):
        return self.n1 * self.n2

    def dividirNumeros(self):
        #Revisa que no se haga una division por cero
        try:
            self.n1 / self.n2
        except ZeroDivisionError as e:
            print("Error dividiendo por zero")
        else:
            return self.n1 / self.n2


    def aplicarOperacion(self,operacion):
        match operacion:
            case "+":
                return self.sumarNumeros()
            case "-":
                return self.restarNumeros()
            case "*":
                return self.multiplicarNumeros()
            case "/":
                return self.dividirNumeros()
            case _:
                return None

class Calculo:
    @staticmethod
    def main():
        print("------Calculadora-------")
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))

        operacion = OperacionMatematica(valor1, valor2)
        simbolo = input("Ingrese la operación a realizar.\n ('+', '-', '*', '/'): ")
        while simbolo not in ("+", "-", "*", "/"):
            print("Símbolo no válido.")
            simbolo = input("Ingrese la operación a realizar.\n ('+', '-', '*', '/'): ")

        resultado = operacion.aplicarOperacion(simbolo)
        if resultado is not None:
            print(f"{valor1} {simbolo} {valor2} = {resultado}")
        else:
            print("Operación fallida.")



if __name__ == "__main__":
    Calculo.main()
