class OperacionMatematica:
    def sumarNumeros(self,num1,num2):
        return num1 + num2
    def restarNumeros(self,num1,num2):
        return num1 - num2
    def multiplicarNumeros(self,num1,num2):
        return num1 * num2
    def dividirNumeros(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    def aplicaroperacion(self,operacion,num1, num2):
        if operacion == "+":
            return self.sumarNumeros(num1, num2)
        elif operacion == "-":
            return self.restarNumeros(num1,num2)
        elif operacion == "*":
            return self.multiplicarNumeros(num1,num2)
        elif operacion == "/":
            return self.dividirNumeros(num1, num2)
        else:
            return "operacion no valida"
def main():
    operacion_matematica = OperacionMatematica()
    num1 = int(input("Ingrese un numero"))
    num2 = int(input("Ingrese otro numero"))
    operacion = input("ingrese: (+), (-), (*), (/): ")
    resultado = operacion_matematica.aplicaroperacion(operacion, num1, num2)
    print(f"El resultado de la operación es: {resultado}")

if __name__ == "__main__":
    main()


