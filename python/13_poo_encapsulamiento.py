class Guerrero:
    nombre: str
    __poder: int

    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.__poder = poder

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Poder:", self.__poder)

goku = Guerrero("Goku", 9900)
vegeta = Guerrero("Vegeta", 8800)
picolo = Guerrero("Piccolo", 7700)
josue = Guerrero("Josue", 7777)

goku.mostrar_info()
print("---")
vegeta.mostrar_info()
print("---")
picolo.mostrar_info()
print("---")
josue.mostrar_info()
print("---")

print(vegeta.nombre)
print(vegeta.get(poder))