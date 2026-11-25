print("Condicional if")
print("Condiconal Simple")
dinero=10
if dinero>=5:
    print("Homero puede comprar rosquillas")
print("Programa finalizó")

print("Condicional If - else")
print("Condicional Dos Caminos")
creditos = float(input("Cantidad de creditos disponibles"))
precio_repuesto = float(input("Precio repuesto"))

if (creditos >= precio_repuesto):
    print("Compra Autorizada")
else:
    print("Créditos insuficientes")
    print("Buscar solucion o trueque")


print("Condicional If - elif - else")
print("Condicional Condiciones Anidadas")
combustible = float(input("Combustible de la nave"))

if (combustible >= 75):
    print("Óptimo")
elif (combustible >= 50):
    print("Suficiente")
elif (combustible >= 20):
    print("Bajo")
else:
    print("Critico")
    print("Localiza base mas cercana")


print("Condicional CONDICIONES ANINADAS")
piloto = input("Nombre del Piloto")
motor_funciona = input("El motor funciona (SI/NO)")
combustible = int(input("Combustible disponible"))

if (motor_funciona=="SI"):
    print("Motor Verificado")
    if combustible>=50:
        print("Combustible suficiente")
        print("Participación Autorizada")
    else:
        print("Debe recargar combustible")
else:
    print("No puede participar")
    print("El motor necesita reparación")

print(" Condicional Condiciones Anidadas")