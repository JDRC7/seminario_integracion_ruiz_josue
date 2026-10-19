print("CRUD DE LISTAS EN PYTHON")

avengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitan America", "estado": "Activo"},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": "Activo"}
]

def create():
    id_nuevo = len(avengers) + 1
    print("\n--- Reclutar Avenger ---")
    nombre = input("Nombre real: ")
    heroe = input("Heroe: ")
    estado = input("Estado (Activo, Retirado, Desaparecido): ")
    
    nuevo_avenger = {
        "id": id_nuevo,
        "nombre": nombre,
        "heroe": heroe,
        "estado": estado
    }
    avengers.append(nuevo_avenger)
    print("¡Avenger agregado con éxito!")

def read():
    print("\n--- Lista de Avengers ---")
    for avenger in avengers:
        print(f"ID: {avenger['id']} | Nombre: {avenger['nombre']} | Héroe: {avenger['heroe']} | Estado: {avenger['estado']}")

def update():
    print("\n--- Actualizar Avenger ---")
    id_update = int(input("Ingrese el ID a modificar: "))
    encontrado = False
    for avenger in avengers:
        if avenger["id"] == id_update:
            avenger["nombre"] = input("Nuevo nombre real: ")
            avenger["heroe"] = input("Nuevo héroe: ")
            avenger["estado"] = input("Nuevo estado: ")
            print("¡Actualizado con éxito!")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un Avenger con ese ID.")

def delete():
    print("\n--- Eliminar Avenger ---")
    id_delete = int(input("Ingrese el ID a borrar: "))
    encontrado = False
    for avenger in avengers:
        if avenger["id"] == id_delete:
            avengers.remove(avenger)
            print("¡Avenger eliminado!")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un Avenger con ese ID.")

def menu():
    while True:
        print("\n=== Menú Avengers ===")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1 al 5): ")
        
        if opcion == "1":
            create()
        elif opcion == "2":
            read()
        elif opcion == "3":
            update()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()