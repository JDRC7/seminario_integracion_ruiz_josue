
print("===== INGRESAR DATOS DEL ESTUDIANTE =====")

nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")
print("Bienvenido al Sistema de Notas Escolares")
print(f"Hasta luego {nombre}\n")


# SECCIÓN DE CALIFICACIONES
print("===== REGISTRO DE CALIFICACIONES =====")

cantidad_notas = int(input("¿Cuántas notas tienes registradas? "))

total_notas = cantidad_notas + 2

print("Notas totales:", total_notas)


# CONVERSIONES
print("\n===== SISTEMA DE MATRÍCULAS =====")

nombre_estudiante = input("Nombre del estudiante: ")

materias = int(input("Cantidad de materias: "))

costo_materia = float(input("Costo por materia: "))

total = materias * costo_materia

print("Total a pagar:", total)

print("Total a pagar (round):", round(total, 2))

print(f"Total a pagar para {nombre_estudiante}: ${total:.2f}")
