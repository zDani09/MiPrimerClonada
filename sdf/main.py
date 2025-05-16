from Clientes import Cliente
from Equipos import Equipo

def ingresar_cliente():
    apellidos = input("Ingrese los apellidos del cliente: ")
    nombres = input("Ingrese los nombres del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    cliente = Cliente(apellidos, nombres, telefono)
    return cliente

def ingresar_equipo():
    numero_parte = input("Ingrese el número de parte del equipo: ")
    tipo_equipo = input("Ingrese el tipo de equipo (ejemplo: teléfono, portátil, pc de escritorio): ")
    descripcion = input("Ingrese la descripción del problema del equipo: ")
    equipo = Equipo(numero_parte, tipo_equipo, descripcion)
    return equipo

def mostrar_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes:
            print(f"{cliente.nombres} {cliente.apellidos} - Teléfono: {cliente.telefono}")
            cliente.ver_equipos()

def ver_equipos_por_cliente(clientes):
    apellidos_cliente = input("Ingrese los apellidos del cliente para ver sus equipos: ")
    encontrado = False
    for cliente in clientes:
        if cliente.apellidos == apellidos_cliente:
            encontrado = True
            cliente.ver_equipos()
            break
    if not encontrado:
        print(f"No se encontró un cliente con los apellidos: {apellidos_cliente}")

def main():
    clientes = []  
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar Cliente")
        print("2. Ver Clientes")
        print("3. Agregar Equipo")
        print("4. Ver Equipos de un Cliente")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            cliente = ingresar_cliente()
            clientes.append(cliente)
        
        elif opcion == '2':
            mostrar_clientes(clientes)
        
        elif opcion == '3':
            cliente_nombre = input("Ingrese los apellidos del cliente para agregar un equipo: ")
            cliente_encontrado = False
            for cliente in clientes:
                if cliente.apellidos == cliente_nombre:
                    cliente_encontrado = True
                    equipo = ingresar_equipo()
                    cliente.agregar_equipo(equipo)
                    print("Equipo agregado correctamente.")
                    break
            if not cliente_encontrado:
                print("No se encontró el cliente con los apellidos proporcionados.")
        
        elif opcion == '4':
            ver_equipos_por_cliente(clientes)
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()