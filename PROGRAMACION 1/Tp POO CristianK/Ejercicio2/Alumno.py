from Nota import  Nota
class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def ingresoNota(self,nota):
        self.notas.append(nota)
    
    def promedioNotas(self):
        suma = 0
        for nota in self.notas:
            suma += nota.notaExamen
        return suma/len(self.notas)
    
    def __str__(self):
        lista_notas = "".join( [f"\n{nota}\n " for nota in self.notas] )
        return  f"---\nNombre: {self.nombreCompleto},\nLegajo: {self.legajo},\nNotas:\n{lista_notas}\n"
