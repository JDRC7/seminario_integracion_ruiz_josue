print("Incluir Datos con Input")
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")
print("Bienvenido a Springfield")
print(f"Hasta luego {nombre}\n")

# SECCIÓN ROSQUILLAS
cantidad = int(input("¿Cuántas rosquillas hay? "))
total_rosquillas = cantidad + 2  # Se guarda el resultado en una variable
print("Rosquillas totales:", total_rosquillas)

print("\nCONVERSIONES")
print("=== TIENDA DE APU ===")
nombre_cliente = input("Nombre del cliente: ")  # Sin espacios en la variable
unidades = int(input("Cantidad de productos: "))
precio = float(input("Precio unitario: "))

total = unidades * precio
print("Total a pagar: ", total)
print("Total a pagar (round); ", round(total,2))
print(f"Total a pagar para {nombre_cliente}: ${total:.2f}")