
"""
Manejo de Cadena de Caracteres
Sistema de Notas Escolares
"""

nombre1 = "Roberto Rocha"
print(f"Estudiante 1: {nombre1}")
print(f"Tipo de datos: {type(nombre1)}")

nombre2 = "María López"
print(f"Estudiante 2: {nombre2}")
print(f"Tipo de datos: {type(nombre2)}")


print("Funciones comunes de texto")

estudiante_1 = "Roberto"
estudiante_2 = "María"

longitud_estudiante_1 = len(estudiante_1)
longitud_estudiante_2 = len(estudiante_2)

print("Nombre estudiante 1:", estudiante_1)
print("Longitud estudiante 1:", longitud_estudiante_1)

print("Nombre estudiante 2:", estudiante_2)
print("Longitud estudiante 2:", longitud_estudiante_2)


print("Convertir Mayúsculas y minúsculas")

mensaje = "El estudiante ha aprobado el examen de matemáticas"

mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()

print("Mensaje Original:", mensaje)
print("Mensaje en Mayúscula:", mensaje_mayuscula)
print("Mensaje en Minúscula:", mensaje_minuscula)


print("Reemplazo de substring")

mensaje = "Roberto está cursando el décimo año"

nuevo_mensaje = mensaje.replace("décimo", "primero")

print("Mensaje Original:", mensaje)
print("Mensaje Modificado:", nuevo_mensaje)


# Separar materias
materias = "Matemáticas,Ciencias,Lengua,Inglés"

print("Materias:", materias)

lista_materias = materias.split(",")

print(lista_materias)

print("Primera materia:", lista_materias[0])


print("Extraer subcadenas")

mensaje = "Roberto ha aprobado matemáticas"

estudiante = mensaje[0:7]
resultado = mensaje[12:20]

print("Nombre del estudiante:", estudiante)
print("Resultado académico:", resultado)
