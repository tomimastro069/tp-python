from Nota import  Nota
class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def ingresoNota(self,notas):
        self.notas = notas
    
    def __str__(self):
        notas_str = ", ".join(str(nota) for nota in self.notas)
        return  f"---\nNombre: {self.nombreCompleto},\nLegajo: {self.legajo},\nNotas: {notas_str}\n---"
