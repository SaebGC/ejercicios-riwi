total_dia = 0

while True:
    subtotal = 0
    producto = input("Ingrese el producto que desea comprar: ").lower()
    if producto == "salir":
        break
    cantidad = int(input("Ingrese la cantidad del producto: "))

    if producto == "cafe":
        subtotal += 4000 * cantidad

    elif producto == "capuchino":
        subtotal += 7000 * cantidad

    elif producto == "pastel":
        subtotal += 6000 * cantidad
    else:
        print("Aun no contamos con ese producto")

    if subtotal > 20000:
        subtotal *= 0.90
    total_dia += subtotal

    print(f"Subtotal de su compra: {subtotal} pesos")
    print("Gracias por su compra. ¡Vuelva pronto!")
print(f"Total del día: {total_dia} pesos")
