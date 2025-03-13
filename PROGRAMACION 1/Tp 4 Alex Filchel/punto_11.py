productos = {
    "A001" : ("Remera", 150),
    "A002" : ("Bicicleta", 900),
    "A003" : ("Mousepad", 230),
    "A004" : ("Reloj", 300),
    "A005" : ("Monitor", 1500)
}

def mostrar_inventario(productos):
    for i in productos:
        print(f"Codigo: {i}, Descripcion: {productos[i]}\n")
    
def buscar_producto(productos):
    while True:
        codigo = input("Ingrese el codigo del producto: ")
        if codigo in productos:
            print(f"Producto encontrado: {productos[codigo]}")
            break
        else:
            print("Error, codigo incorrecto")

def modificar_precio(productos):
    while True:
        codigo = input("Ingrese el codigo del producto: ")
        if codigo in productos:
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            nuevo_producto = (productos[codigo][0], nuevo_precio)
            productos[codigo] = nuevo_producto
            print("Precio Actualizado.")
            break
        else:
            print("Error, codigo incorrecto")
    for i in productos:
        print(f"Codigo: {i}, Descripcion: {productos[i]}\n")

def eliminar_producto(productos):
    while True:
        codigo = input("Ingrese el codigo del producto: ")
        if codigo in productos:
            productos.pop(codigo)
            print("Producto Eliminado.")
            break
        else:
            print("Error, codigo incorrecto")
    for i in productos:
        print(f"Codigo: {i}, Descripcion: {productos[i]}\n")

def productos_por_rango_de_precio(productos):
    min_precio = int(input("Ingrese el precio minimo del rango: "))
    max_precio = int(input("Ingrese el precio maximo del rango: "))

    print(f"Productos entre ${min_precio} y ${max_precio}")
    for i in productos:
        if productos[i][1] > min_precio and productos[i][1] < max_precio:
            print(f"Codigo: {i}, Descripcion: {productos[i]}\n")

def main():
    while True:
        try:
            decision = int(input("""
                                 1: Mostrar Inventario
                                 2: Buscar Producto
                                 3: Modificar Precio
                                 4: Eliminar Producto
                                 5: Buscar productos por rango de precio\n
                                 Que accion desea realizar: """))
            break
        except ValueError:
            print("ERROR, ingrese un numero valido")
    if decision == 1:
        mostrar_inventario(productos)
    elif decision == 2:
        buscar_producto(productos)
    elif decision == 3:
        modificar_precio(productos)
    elif decision == 4:
        eliminar_producto(productos)
    else:
        productos_por_rango_de_precio(productos)

main()
        