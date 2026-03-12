contador = 0
for i in range(6):
    producto = input("Ingrese el producto que desea comprar: ")
    precio = float(input("Ingrese el precio del producto: "))

    if precio > 100000:
        contador = contador + 1
        print(f"El producto {producto} tiene un precio mayor a 100000 pesos.")

print(f"En total, hay {contador} productos con un precio mayor a 100000 pesos.")