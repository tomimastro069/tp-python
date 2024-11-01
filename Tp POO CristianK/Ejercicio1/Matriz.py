from Celda import Celda
class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def ingresarCeldas(self,fila,col,valor):
        celda = Celda(fila,col,valor)

        #se asegura que exista la lista filas
        while fila >= len(self.celdasMatriz):
            self.celdasMatriz.append([])
        
        #se segura que exista la lista columna
        while col >= len(self.celdasMatriz[fila]):
            self.celdasMatriz[fila].append(None)
        
        self.celdasMatriz[fila][col] = celda

    def mostrarCeldas(self):
        for  fila in self.celdasMatriz:
            print([celda.valor if celda else None for celda in fila])