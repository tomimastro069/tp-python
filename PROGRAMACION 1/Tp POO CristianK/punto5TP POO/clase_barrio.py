from clase_vivienda import Vivienda

class Barrio:
    def __init__(self, nombre: str, empresaConstructora: str):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []
        
    def getSuperficieTotalTerreno(self) -> float:
        return sum(vivienda.superficieTerreno for vivienda in self.viviendas)

    def agregarVivienda(self, vivienda: Vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerrenoXManzana(self, manzana: str) -> float:
        return sum(vivienda.superficieTerreno for vivienda in self.viviendas if vivienda.manzana == manzana)

    def getSuperficieTotalCubierta(self) -> float:
        return sum(vivienda.getMetrosCuadradosCubiertos() for vivienda in self.viviendas)

