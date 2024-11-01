from Alumno import Alumno
from metodos import numeroPositivoEntero,numeroPositivoFlotante
from Nota import Nota
class CargaNotas: 
    lista_alumnos = []

    @staticmethod
    def main():
        CargaNotas.cargaNotas()
        CargaNotas.mostrar()

    @staticmethod
    def  cargaNotas():
        while(True):
            nombre = input("Ingrese el nombre completo del alumno: ")
            if nombre == "FIN":
                break
            legajo = numeroPositivoEntero("Ingrese el legajo: ")
            while(True):
                lista_notas = list()
                cantNotas = int(input("Ingresa la cantidad de notas: "))
                for  i in range(cantNotas):
                    catedra =  input("Ingrese la catedra: ")
                    nota = numeroPositivoFlotante(f"Ingrese la nota {i+1}: ")
                    nota1 = Nota(catedra,nota)
                    lista_notas.append(nota1)
                if  len(lista_notas) == cantNotas:
                    break
            alumno = Alumno(nombre,legajo)  
            alumno.ingresoNota(lista_notas)
            CargaNotas.lista_alumnos.append(alumno)
                    

    @staticmethod
    def mostrar():
        for i in  range(len(CargaNotas.lista_alumnos)):############
            print(CargaNotas.lista_alumnos[i])

CargaNotas.main()