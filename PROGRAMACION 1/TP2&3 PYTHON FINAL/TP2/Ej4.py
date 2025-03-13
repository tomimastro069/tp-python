class programacajera:
    def __init__(self, Precio):

        self.Precio = Precio

        self.monedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]

        self.resultado = {}


    def calculo(self):

        cantidad_faltante = self.Precio
        
        for i in self.monedas:
            if cantidad_faltante >= i:
                cantidad_billetes = cantidad_faltante // i
                cantidad_faltante = round(cantidad_faltante % i, 2)
                self.resultado[i] = int(cantidad_billetes)
            else:
                self.resultado[i] = 0

    def mostrar_resultado(self):
        for i, cantidad in self.resultado.items():
            if i >= 1:
                print(f"{cantidad} billetes de {i}")
            else:
                print(f"{cantidad} monedas de {i}")

Precio = float(input("Ingrese la cantidad de dinero: "))

cajera = programacajera(Precio)

cajera.calculo()

cajera.mostrar_resultado()
