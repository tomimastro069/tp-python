"""19- Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un
atributo de nombre operación.
Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:
sumarNumeros()
restarNumeros()
multiplicarNumeros()
dividirNumeros()
El quinto método será el siguiente:
aplicarOperacion(operacion){
…………………..
}
Cree una clase Calculo que contenga un método main, donde cree una instancia de la
clase OperacionMatematica, asigne 2 valores para las variables de la instancia y
ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “-
”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las
operaciones. """

class OperacionMatematica:
    def __init__(self, valor1, valor2, operacion):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = operacion
        self.resultado = None

    def sumar_Numeros(self):
        self.resultado = self.valor1 + self.valor2

    def restar_Numeros(self):
        if self.valor1 > self.valor2:
            self.resultado = self.valor1 - self.valor2
        else:
            self.resultado = self.valor2 - self.valor1

    def multiplicar_Numeros(self):
        self.resultado = self.valor1 * self.valor2

    def dividir_Numeros(self):
        if self.valor2 != 0:
            self.resultado = float(self.valor1 / self.valor2)
        else:
            raise ValueError("No se puede dividir por cero.")

    def aplicar_Operacion(self):
        if self.operacion == "+":
            self.sumar_Numeros()
        elif self.operacion == "-":
            self.restar_Numeros()
        elif self.operacion == "*":
            self.multiplicar_Numeros()
        elif self.operacion == "/":
            self.dividir_Numeros()
        else:
            raise ValueError("Operación no soportada.")
        return self.resultado

    def obtener_resultado(self):
        return f"{self.valor1} {self.operacion} {self.valor2} = {self.resultado}"

class Calculo:
    @staticmethod 
    def main():
        while True:
            valor1 = int(input("Ingrese el primer valor: "))
            if valor1 == 0:
                print("El primer valor no puede ser cero. Intente de nuevo.")
                continue
            valor2 = int(input("Ingrese el segundo valor: "))
            if valor2 == 0:
                print("El segundo valor no puede ser cero. Intente de nuevo.")
                continue
            break

        operaciones = ["+", "-", "*", "/"]

        for operacion in operaciones:
            calc = OperacionMatematica(valor1, valor2, operacion)
            calc.aplicar_Operacion()
            print(calc.obtener_resultado())

# Ejecutar el método main de la clase Calculo
Calculo.main()