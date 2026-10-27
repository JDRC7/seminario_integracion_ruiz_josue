
# CICLO FOR: REGISTRO DE CALIFICACIONES

for nota in range(1, 6):
    print("Roberto Rocha registra la calificación", nota)


# CICLO FOR: TABLA DE MULTIPLICAR
print("\n===== TABLA DE MULTIPLICAR =====")

for numero in range(1, 11):
    print("Multiplicación ", 5, "*", numero, "=", 5 * numero)


# CICLO FOR CON STEP
print("\n===== CALIFICACIONES IMPARES =====")

for numero in range(1, 11, 2):
    print("Multiplicación ", 5, "*", numero, "=", 5 * numero)


# CRUD DE ESTUDIANTES EN PYTHON
print("\n===== SISTEMA DE NOTAS ESCOLARES =====")

estudiantes = [
    {"id": 1, "nombre": "Roberto Rocha", "nota": 9.5, "estado": "Aprobado"},
    {"id": 2, "nombre": "María López", "nota": 8.5, "estado": "Aprobado"},
    {"id": 3, "nombre": "Carlos Gómez", "nota": 5.5, "estado": "Reprobado"},
]

print("Lista de estudiantes")

for estudiante in estudiantes:
    print(f"{estudiante['id']} - Nombre: {estudiante['nombre']}")

 
# RECORRER UNA LISTA DE ESTUDIANTES
nombres = ["Pedro", "Pablo", "Juan"]

for nombre in nombres:
    print("Estudiante actual:", nombre)


# DICCIONARIO DE ESTUDIANTES Y CALIFICACIONES
calificaciones = {
    "Roberto": 9.5,
    "María": 8.5,
    "Carlos": 6.0,
    "Pedro": 4.5
}

for nombre, nota in calificaciones.items():
    if nota >= 7:
        print(nombre, "ha aprobado la materia")
    else:
        print(nombre, "necesita recuperación")


# CICLOS FOR ANIDADOS
estudiantes = ["Roberto", "María", "Carlos", "Pedro", "Pablo"]

for estudiante in estudiantes:
    print("Turno de evaluación:", estudiante)

    for examen in range(1, 4):
        print("Examen:", examen)


# BREAK Y CONTINUE
print("\n===== BREAK Y CONTINUE =====")

for estudiante in estudiantes:

    if estudiante == "Carlos":
        break

    if estudiante == "María":
        continue

    print("Estudiante evaluado:", estudiante)
