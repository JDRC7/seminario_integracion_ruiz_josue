
class Persona:
    nombre: str
    curso: str

    def __init__(self, nombre: str, curso: str):
        self.nombre = nombre
        self.curso = curso

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Curso:", self.curso)


# CLASE HIJA
class Estudiante(Persona):

    def __init__(self, nombre: str, curso: str):
        super().__init__(nombre, curso)

    def muestra_nombre(self):
        print("Nombre del estudiante:", self.nombre)


# CREACIÓN DE OBJETOS
roberto = Estudiante("Roberto Rocha", "Décimo Año")
maria = Estudiante("María López", "Noveno Año")


# MOSTRAR INFORMACIÓN
roberto.mostrar_info()
maria.mostrar_info()

# MOSTRAR NOMBRES
roberto.muestra_nombre()
maria.muestra_nombre()
