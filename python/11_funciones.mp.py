
print("FUNCIONES")
print("Autor: Josue Ruiz")
print("Sistema de Notas Escolares")


# FUNCIÓN SIN PARÁMETROS
def registrar_notas():
    print("El estudiante registra sus calificaciones")
    print("Registro de notas completado")


registrar_notas()
registrar_notas()
registrar_notas()
registrar_notas()


# FUNCIÓN CON PARÁMETROS
def evaluar_estudiante(estudiante):
    print(estudiante, "realiza una evaluación")


evaluar_estudiante("Roberto Rocha")
evaluar_estudiante("María López")
evaluar_estudiante("Carlos Gómez")
evaluar_estudiante("Josue Ruiz")


# FUNCIÓN CON PARÁMETROS Y RETORNO
def calcular_promedio(nota1, nota2):
    promedio = (nota1 + nota2) / 2
    return promedio


resultado = calcular_promedio(8, 9)
print("El promedio de Josue Ruiz es:", resultado)

resultado = calcular_promedio(10, 9.5)
print("El promedio de Roberto Rocha es:", resultado)


# FUNCIÓN CON CONDICIONALES
def clasificar_estudiante(nombre, nota):

    if nota >= 9:
        print(f"¡Excelente rendimiento académico de {nombre}!")

    else:
        print(f"{nombre} necesita mejorar sus calificaciones.")


clasificar_estudiante("Josue Ruiz", 9.5)
clasificar_estudiante("Gohan", 8.5)
clasificar_estudiante("Yamcha", 4.0)


# VARIABLES CON TIPOS DE DATOS
nombre_estudiante: str = "Roberto Rocha"
edad: int = 15
nota: float = 8.5
esta_aprobado: bool = True


# FUNCIÓN CON ANOTACIONES DE TIPOS
def calcular_nota_final(
    nota1: float,
    nota2: float
) -> float:

    return (nota1 + nota2) / 2


promedio: float = calcular_nota_final(9.0, 8.5)

print("Estudiante:", nombre_estudiante)
print("Edad:", edad)
print("¿Está aprobado?:", esta_aprobado)
print("Promedio calculado:", promedio)
