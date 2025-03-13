class Nota:
    def __init__(self, catedra,notaExamen):
        self.catedra = catedra
        self.notaExamen = notaExamen
    def __str__(self):
        return f"{self.catedra}: {self.notaExamen}"