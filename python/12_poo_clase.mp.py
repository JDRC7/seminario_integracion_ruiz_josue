
class Estudiante:
    nombre: str
    curso: str

    def __init__(self, nombre: str, curso: str):
        self.nombre = nombre
        self.curso = curso

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Curso:", self.curso)


# CREACIÓN DE OBJETOS

roberto = Estudiante("Roberto Rocha", "Décimo Año")
maria = Estudiante("María López", "Noveno Año")
carlos = Estudiante("Carlos Gómez", "Octavo Año")
josue = Estudiante("Josue Ruiz", "Séptimo Año")


# MOSTRAR INFORMACIÓN DE LOS ESTUDIANTES

roberto.mostrar_info()
print("---")

maria.mostrar_info()
print("---")

carlos.mostrar_info()
print("---")

josue.mostrar_info()
print("---")
