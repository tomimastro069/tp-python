class SumaDedigitos:
    def __init__(self, numero):
        self.numero = numero

        self.centena = numero // 100

        self.decena = (numero % 100) // 10

        self.unidad1 = numero % 10

        self.suma = self.centena + self.decena + self.unidad1

    def sumar(self):
        print(f"{self.centena} +  {self.decena}  + {self.unidad1} = {self.suma}")

numero= int(input("ingrese un numero de 3 digitos (100 / 999)"))

while numero < 100 or numero > 999:
    print ("ingrese un numero valido")

    numero= int(input("ingrese un numero de 3 digitos (100 / 999)"))

numero1= SumaDedigitos(numero)

numero1.sumar()

