
# CICLO WHILE: MEJORAR LAS CALIFICACIONES

nota = 2

while nota < 10:
    print("Roberto Rocha está mejorando su calificación")
    nota += 2

print("¡Roberto Rocha alcanzó la nota máxima!")


# CICLO WHILE: DISMINUIR PUNTOS DE RECUPERACIÓN

puntos = 2000

while puntos > 0:
    print("El estudiante tiene", puntos, "puntos acumulados")
    puntos -= 500

print("El estudiante se quedó sin puntos de recuperación")


# CONTINUE Y BREAK
print("\n===== CONTINUE Y BREAK =====")

dia = 0

while dia < 8:
    dia += 1

    if dia == 4:
        print("Día 4: Roberto tiene examen de Matemáticas")
        continue

    print("Día", dia, "Roberto asiste a clases")

    if dia == 8:
        print("Fin de la semana escolar")
        break


# CICLO FOR: REVISIÓN DE NOTAS POR MATERIA
print("\n===== REVISIÓN DE NOTAS ESCOLARES =====")

for materia in range(1, 11):

    if materia == 3:
        print(f"Materia {materia}: pendiente de evaluación, se omite")
        continue

    if materia == 7:
        print(f"Materia {materia}: revisión final de calificaciones")
        break

    print(f"Materia {materia}: evaluación realizada normalmente")
