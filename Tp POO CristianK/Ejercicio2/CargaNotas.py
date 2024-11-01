from Alumno import Alumno
from metodos import numeroPositivoEntero,numeroPositivoFlotante
from Nota import Nota
import os
class CargaNotas: 
    lista_alumnos = []

    @staticmethod
    def main():
        CargaNotas.cargaNotas()
        os.system("cls")
        CargaNotas.mostrar()

    @staticmethod
    def  cargaNotas():
        while(True):
            nombre = input("Ingrese el nombre completo del alumno: ")
            if nombre == "FIN":
                break
            legajo = numeroPositivoEntero("Ingrese el legajo: ")
            alumno = Alumno(nombre,legajo)
            while True:
                catedra =  input("Ingrese la catedra: ")
                nota = numeroPositivoFlotante(f"Ingrese la nota: ")
                nota1 = Nota(catedra,nota)
                alumno.ingresoNota(nota1)           
                respuesta = input("Desea ingresar otra nota? (S/N): ")
                if respuesta in ("N","n"):
                    break
            CargaNotas.lista_alumnos.append(alumno)

    @staticmethod
    def mostrar():
        for alumno in CargaNotas.lista_alumnos:
            print(alumno)
            print("Promedio: ",alumno.promedioNotas(),"\n")

CargaNotas.main()