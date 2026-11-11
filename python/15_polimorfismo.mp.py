
class Persona:
    nombre: str
    curso: str

    def __init__(self, nombre: str, curso: str):
        self.nombre = nombre
        self.curso = curso

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Curso:", self.curso)


class Estudiante(Persona):

    def __init__(self, nombre: str, curso: str):
        super().__init__(nombre, curso)

    # Sobrescritura del método mostrar_info()
    def mostrar_info(self):
        print(
            "Estudiante:", self.nombre,
            "Curso:", self.curso
        )


# CREACIÓN DE OBJETOS
roberto = Estudiante("Roberto Rocha", "Décimo Año")
maria = Estudiante("María López", "Noveno Año")


# MOSTRAR INFORMACIÓN
roberto.mostrar_info()
maria.mostrar_info()
