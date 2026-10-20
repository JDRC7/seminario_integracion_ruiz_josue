
print("CRUD DE ESTUDIANTES EN PYTHON")

estudiantes = [
    {"id": 1, "nombre": "Roberto Rocha", "curso": "Décimo Año", "nota": 9.5, "estado": "Aprobado"},
    {"id": 2, "nombre": "María López", "curso": "Noveno Año", "nota": 8.5, "estado": "Aprobado"},
    {"id": 3, "nombre": "Carlos Gómez", "curso": "Octavo Año", "nota": 5.5, "estado": "Reprobado"}
]


# CREATE: Registrar estudiante
def create():
    id_nuevo = max([e["id"] for e in estudiantes], default=0) + 1

    print("\n--- Registrar Estudiante ---")

    nombre = input("Nombre del estudiante: ")
    curso = input("Curso: ")
    nota = float(input("Nota (sobre 10): "))

    if nota >= 7:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    nuevo_estudiante = {
        "id": id_nuevo,
        "nombre": nombre,
        "curso": curso,
        "nota": nota,
        "estado": estado
    }

    estudiantes.append(nuevo_estudiante)

    print("¡Estudiante registrado con éxito!")


# READ: Mostrar estudiantes
def read():
    print("\n--- Lista de Estudiantes ---")

    for estudiante in estudiantes:
        print(
            f"ID: {estudiante['id']} | "
            f"Nombre: {estudiante['nombre']} | "
            f"Curso: {estudiante['curso']} | "
            f"Nota: {estudiante['nota']} | "
            f"Estado: {estudiante['estado']}"
        )


# UPDATE: Modificar estudiante
def update():
    print("\n--- Actualizar Estudiante ---")

    id_update = int(input("Ingrese el ID a modificar: "))
    encontrado = False

    for estudiante in estudiantes:
        if estudiante["id"] == id_update:

            estudiante["nombre"] = input("Nuevo nombre: ")
            estudiante["curso"] = input("Nuevo curso: ")
            estudiante["nota"] = float(input("Nueva nota: "))

            if estudiante["nota"] >= 7:
                estudiante["estado"] = "Aprobado"
            else:
                estudiante["estado"] = "Reprobado"

            print("¡Estudiante actualizado con éxito!")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró un estudiante con ese ID.")


# DELETE: Eliminar estudiante
def delete():
    print("\n--- Eliminar Estudiante ---")

    id_delete = int(input("Ingrese el ID a eliminar: "))
    encontrado = False

    for estudiante in estudiantes:
        if estudiante["id"] == id_delete:
            estudiantes.remove(estudiante)

            print("¡Estudiante eliminado correctamente!")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró un estudiante con ese ID.")


# MENÚ PRINCIPAL
def menu():
    while True:

        print("\n=== SISTEMA DE NOTAS ESCOLARES ===")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Modificar estudiante")
        print("4. Eliminar estudiante")
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
            print("Saliendo del sistema escolar...")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# Ejecutar el menú principal
if __name__ == "__main__":
    menu()