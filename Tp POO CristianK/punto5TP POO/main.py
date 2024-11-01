from clase_barrio import Barrio
from clase_vivienda import Vivienda
from clase_habitacion import Habitacion

barrio = Barrio("Barrio Elegante", "Constructora XYZ")

vivienda1 = Vivienda("Calle Falsa", 123, "Manzana A", 1, 200.0)
vivienda1.agregarHabitacion(Habitacion("Habitación 1", 50.0))
vivienda1.agregarHabitacion(Habitacion("Habitación 2", 60.0))

vivienda2 = Vivienda("Calle Verdadera", 456, "Manzana B", 2, 150.0)
vivienda2.agregarHabitacion(Habitacion("Habitación 1", 30.0))
vivienda2.agregarHabitacion(Habitacion("Habitación 2", 40.0))


barrio.agregarVivienda(vivienda1)
barrio.agregarVivienda(vivienda2)


print(f"Superficie total de terreno del barrio: {barrio.getSuperficieTotalTerreno()} m²")
print(f"Superficie total de terreno de Manzana A: {barrio.getSuperficieTotalTerrenoXManzana('Manzana A')} m²")
print(f"Superficie total cubierta del barrio: {barrio.getSuperficieTotalCubierta()} m²")