class Guerrero:
    nombre: str
    raza: str

    def __init__(self, nombre: str, raza: str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Raza:", self.raza)

goku = Guerrero("Goku", "Sayajin")
vegeta = Guerrero("Vegeta", "Sayajin")
picolo = Guerrero("Piccolo", "Namekusein")
josue = Guerrero("Josue", "kAYOSAMA")


goku.mostrar_info()
print("---")
vegeta.mostrar_info()
print("---")
picolo.mostrar_info()
print("---")
josue.mostrar_info()
print("---")
