
print("COLECCIONES DE DATOS")

# LISTAS
print("Listas")

estudiantes = ["Roberto", "María", "Carlos"]

print("Estudiantes:", estudiantes)
print("Tipo:", type(estudiantes))


# TUPLAS
print("Tuplas")

notas = (8.5, 9.0, 7.5)

print("Notas:", notas)
print("Tipo:", type(notas))


# DICCIONARIOS
print("Diccionario")

estudiante = {
    "nombre": "Roberto Rocha",
    "curso": "Décimo Año",
    "aprobado": True
}

print("Estudiante:", estudiante)
print("Tipo:", type(estudiante))


# CONJUNTOS
print("Conjunto")

materias = {
    "Matemáticas",
    "Ciencias",
    "Lengua"
}

print("Materias:", materias)
print("Tipo:", type(materias))


# CRUD DE ESTUDIANTES EN PYTHON

print("\nCRUD DE ESTUDIANTES EN PYTHON")

estudiantes = [
    {
        "id": 1,
        "nombre": "Roberto Rocha",
        "curso": "Décimo Año",
        "estado": "Aprobado"
    },
    {
        "id": 2,
        "nombre": "María López",
        "curso": "Décimo Año",
        "estado": "Aprobado"
    },
    {
        "id": 3,
        "nombre": "Carlos Gómez",
        "curso": "Noveno Año",
        "estado": "Reprobado"
    }
]


# CREATE: Registrar estudiante
def create():
    id = len(estudiantes) + 1

    print("Registrar estudiante")

    nombre = input("Nombre del estudiante: ")
    curso = input("Curso: ")
    estado = input("Estado (Aprobado, Reprobado): ")

    nuevo_estudiante = {
        "id": id,
        "nombre": nombre,
        "curso": curso,
        "estado": estado
    }

    estudiantes.append(nuevo_estudiante)

    print("Estudiante registrado correctamente")


# READ: Mostrar estudiantes
def read():
    print("\nLista de estudiantes")

    for estudiante in estudiantes:
        print(estudiante)


# UPDATE: Actualizar estudiante
def update():
    id = int(input("Ingrese el ID del estudiante: "))

    for estudiante in estudiantes:
        if estudiante["id"] == id:
            estudiante["nombre"] = input("Nuevo nombre: ")
            estudiante["curso"] = input("Nuevo curso: ")
            estudiante["estado"] = input("Nuevo estado: ")

            print("Estudiante actualizado correctamente")
            return

    print("Estudiante no encontrado")


# DELETE: Eliminar estudiante
def delete():
    id = int(input("Ingrese el ID del estudiante: "))

    for estudiante in estudiantes:
        if estudiante["id"] == id:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado correctamente")
            return

    print("Estudiante no encontrado")


# MENÚ PRINCIPAL
while True:

    print("\n===== SISTEMA DE NOTAS ESCOLARES =====")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Actualizar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        create()

    elif opcion == "2":
        read()

    elif opcion == "3":
        update()

    elif opcion == "4":
        delete()

    elif opcion == "5":
        print("Saliendo del sistema escolar")
        break

    else:
        print("Opción no válida")
