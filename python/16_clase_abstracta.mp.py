
from abc import ABC, abstractmethod


# CLASE ABSTRACTA
class Persona(ABC):

    @abstractmethod
    def calcular_promedio(self):
        pass


# CLASE HIJA
class Estudiante(Persona):

    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_promedio(self):
        promedio = (self.nota1 + self.nota2) / 2
        return promedio


# CREAR OBJETO
roberto = Estudiante("Roberto Rocha", 9.0, 8.5)

# MOSTRAR RESULTADO
print("Estudiante:", roberto.nombre)
print("Promedio:", roberto.calcular_promedio())
