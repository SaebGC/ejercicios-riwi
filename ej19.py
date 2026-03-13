contador_agotado = 0
contador_bajo = 0
contador_normal = 0

for i in range(10):
    nombre = input("Ingrese el nombre del producto: ").lower()
    cantidad = int(input("Ingrese la cantidad disponible: "))

    if cantidad == 0: 
        print("El producto ", nombre, " está agotado.")
        contador_agotado += 1
    elif cantidad >= 1 and cantidad <= 5:
        print("El producto ", nombre, " tiene un stock bajo.")
        contador_bajo += 1
    else:
        print("El producto ", nombre, " tiene un stock normal.")
        contador_normal += 1

print("La cantidad de productos agotados es: ", contador_agotado)
print("La cantidad de productos con stock bajo es: ", contador_bajo)
print("La cantidad de productos con stock normal es: ", contador_normal)