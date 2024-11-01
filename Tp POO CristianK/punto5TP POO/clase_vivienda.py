from clase_habitacion import Habitacion

class Vivienda:
    def __init__(self, calle: str, numero: int, manzana: str, nroCasa: int, superficieTerreno: float):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []

    def agregarHabitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self) -> float:
        total_cubiertos = sum(habitacion.metrosCuadrados for habitacion in self.habitaciones)
        
        if total_cubiertos > self.superficieTerreno:
            raise ValueError("La superficie cubierta no puede ser mayor a la superficie del terreno")
        
        return total_cubiertos
