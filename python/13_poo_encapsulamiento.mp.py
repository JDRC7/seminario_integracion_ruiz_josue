
class Estudiante:
    nombre: str
    __nota: float

    def __init__(self, nombre: str, nota: float):
        self.nombre = nombre
        self.__nota = nota

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.__nota)

    # Método getter para consultar la nota
    def get_nota(self):
        return self.__nota


# CREACIÓN DE OBJETOS

roberto = Estudiante("Roberto Rocha", 9.5)
maria = Estudiante("María López", 8.8)
carlos = Estudiante("Carlos Gómez", 7.7)
josue = Estudiante("Josue Ruiz", 7.0)


# MOSTRAR INFORMACIÓN

roberto.mostrar_info()
print("---")

maria.mostrar_info()
print("---")

carlos.mostrar_info()
print("---")

josue.mostrar_info()
print("---")


# CONSULTAR ATRIBUTOS

print(maria.nombre)

print("Nota de María:", maria.get_nota())
