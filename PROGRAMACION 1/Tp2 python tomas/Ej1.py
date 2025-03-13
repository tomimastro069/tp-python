class Numero1:
    def __init__(self,numero):
        self.numero = numero

        self.Vshort = int(numero)
      
        self.Vint = int(numero)

        self.Vlong = float(numero)
      
        self.Vfloat = float(numero)
        
    def resultado(self):

        print("Valor original:", self.numero)

        print("Valor entero:", self.Vint)
          
        if self.Vshort < -32768 or self.Vshort > 32767:
                print("Valor fuera del rango de 'short' 16 bits")
        else:
                print("Valor short: ", self.Vshort)

        if self.Vlong <= -2**63 or self.Vlong >= 2**63 -1:
            print("Valor fuera de rango de'long' 64 bits")
        else: 
            print("Valor long:", self.Vlong)

        print("Valor real:", self.Vfloat)

Numeroingresado = float(input("ingrese un numero decimal: "))
numerofinal = Numero1(Numeroingresado)
numerofinal.resultado()




