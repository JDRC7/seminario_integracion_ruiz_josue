print("Colecciones de datos")
print("Listas")
naves = ["N-1", "Transporte", "Naboo"]
print("Naves ", naves)
print("tipo: ", type(naves))
print("Tuplas")
coordenadas = (15, 30, 45)
print("coordenadas: ", coordenadas)
print("tipo: ", type(coordenadas))  # Nota: en la imagen muestra type(naves) por error del código original, pero lo ideal es type(coordenadas)
print("Diccionario")
droide = {
    "modelo": "R2-D2",
    "tipo": "Astromecanico",
    "activo": True
}
print("droide: ", droide)
print("tipo: ", type(droide))
print("Conjunto")
planetas = {
    "Naboo",
    "Kmino",
    "Alderan"
}
print("planetas: ", planetas)
print("tipo: ", type(planetas))


print("CRUD DE LISTAS EN PYTHON")
advengers = [
    ("id": 1, "nombre", "Toby Stark", "heroe": "Iron Man", "estado": "Activo"),
    ("id": 2, "nombre", "Steve Rogers", "heroe": "Capitan America", "estado": "Activo"),
    ("id": 3, "nombre", "Thor Odison", "heroe": "Thon", "estado": "Activo")
]

def create():
    id = 4
    print("Reclutar advenger")
    nombre =input("Nombre heroe: ")
    heroe = input("Heroe: ")
    estado = inpujt("Estado (Activo, Retirado, Desaparecido)")
    nuevo advenger = {
        "id": id,
        "nombre": nombre,
        "heroe": heroe,
        "estado": estado
    }
    advengers.append(nuevo_advenger)