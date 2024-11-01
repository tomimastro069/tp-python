golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M's", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10],
]

golosinas_pedidas_lista = [
    ["KitKat", 0],
    ["Chicles", 0],
    ["Caramelos de Menta", 0],
    ["Huevo Kinder", 0],
    ["Chetoos", 0],
    ["Twix", 0],
    ["M&M's", 0],
    ["Papas Lays", 0],
    ["Milkybar", 0],
    ["Alfajor Tofi", 0],
    ["Lata Coca", 0],
    ["Chitos", 0],
    ]

empleados = {
    1100: "Jose Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gaston Garcia"
}

clavesTecnico = ("admin","CCCDDD",2020)

def validar_tupla(clavesTecnico):
    tupla_validada = []
    tupla_validada.append(input("Ingrese la primer clave: "))
    tupla_validada.append(input("Ingrese la segunda clave: "))
    tupla_validada.append(int(input("Ingrese la tercer clave: ")))
    tupla_validada = tuple(tupla_validada)
    
    if tupla_validada == clavesTecnico:
        return True
    else:
        return False
    
def rellenar_golosinas(golosinas):
    codigo = validar_golosina()
    while True:
        try:
            aux = int(input("Ingrese la cantidad de golosinas a rellenar: "))
            if aux < 1:
                print("Error, ingrese un numero positivo.")
            else:
                golosinas[codigo][2] = golosinas[codigo][2] + aux
                print("----------------------------")
                print("Golosinas rellenadas exitosamente")
                print("----------------------------")

                break
        except ValueError:
            print("Error, ingrese un numero valido.")
    main()

def golosinas_pedidas(golosinas_pedidas_lista,codigo,mostrar_golosinas):
    if not(mostrar_golosinas):
        golosinas_pedidas_lista[codigo][1] = golosinas_pedidas_lista[codigo][1] + 1 
    else:
        suma = 0
        for i in golosinas_pedidas_lista:
            if i[1] == 0:
                pass
            else:
                suma += i[1]
                print (i)
        print(f"Total de golosinas pedidas: {suma}")
    
def validar_empleado(empleados):
    while True:
        try:
            legajo = int(input("Ingrese su numero de legajo."))
            if not (legajo in empleados):
                print("Usted no pertenece a la empresa.")
            else:
                return True
        except ValueError:
            print("Ingrese un numero de legajo valido.")

def validar_golosina():
    while True:
        try:
            num_golosina = int(input("Ingrese el numero de golosina: ")) - 1
            if (num_golosina < 0 or num_golosina > 12):
                print("Ingrese un numero de golosina valido.")
            else:
                return num_golosina
        except ValueError:
            print("Ingrese un numero de golosina valido.")

def pedirGolosina(empleados,golosinas):
    validar_empleado(empleados)
    num_golosina = validar_golosina()
    print(f"Seleccionaste la golosina {golosinas[num_golosina][1]}")
    
    if not (golosinas[num_golosina][2] < 0):
        golosinas[num_golosina][2] = golosinas[num_golosina][2] - 1
        print(f"Stock de la golosina: {golosinas[num_golosina][2]}")

    golosinas_pedidas(golosinas_pedidas_lista,num_golosina,False)

    if golosinas[num_golosina][2] < 0:
        opcion = int(input(f"“Lo sentimos la golosina {golosinas[num_golosina][1]} no se encuentra disponible\n1-Seleccionar otra golosina\n2-Salir "))
        
        if opcion == 1:
            pedirGolosina(empleados,golosinas)
        else:
            print("---------------------------")
            main()
    else:
        print("---------------------------")
        main()

def main():
    while True:
        try:
            opcion = int(input("Ingrese que opcion desea realizar\n1-Pedir golosina\n2-Mostrar golosinas\n3-Rellenar golosinas\n4-Apagar Maquina\n"))
            if not (opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4):
                print("Error, ingrese una opcion valida.")
            else:
                break
        except ValueError:
            print("Error, ingrese una opcion valida.")

    if opcion == 1:
        print("---------------------------")
        pedirGolosina(empleados,golosinas)
    elif opcion == 2:
        print("---------------------------")
        for i in golosinas:
            print(i)
        print("---------------------------")
        main()
    elif opcion == 3:
        print("---------------------------")
        if validar_tupla(clavesTecnico):
            rellenar_golosinas(golosinas)
        else:
            print("No tiene permiso para ejecutar la funcion de recarga.")
            main()
    else:
        print("---------------------------\nGolosinas Pedidas: ")
        golosinas_pedidas(golosinas_pedidas_lista,0,True)
        print("---------------------------\nMaquina apagada.")

if __name__ == "__main__":
    main()