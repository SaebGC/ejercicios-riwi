caja_alimento = 0
caja_juguete = 0
caja_accesorio = 0
    
for i in range(10):
    while True:
        categoria = input("Ingrese la categoría (alimento, juguete, accesorio): ").lower()
        if categoria == "alimento" or categoria == "juguete" or categoria == "accesorio":
            break
        print("Error: Ingrese una categoría válida (alimento, juguete, accesorio).")
    
    while True:
        try:
            valor_producto = float(input("Ingrese el valor del producto: "))
            if valor_producto < 0:
                print("Error: El valor no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    if categoria == "alimento":
        caja_alimento += valor_producto
    elif categoria == "juguete":
        caja_juguete += valor_producto
    elif categoria == "accesorio":
        caja_accesorio += valor_producto

print("El total de ventas es: ", caja_alimento + caja_juguete + caja_accesorio)
print("El total de ventas de alimento es: ", caja_alimento)
print("El total de ventas de juguete es: ", caja_juguete)
print("El total de ventas de accesorio es: ", caja_accesorio)

if caja_alimento > caja_juguete and caja_alimento > caja_accesorio:
    print("La categoría con más ventas es: alimento")
elif caja_juguete > caja_alimento and caja_juguete > caja_accesorio:
    print("La categoría con más ventas es: juguete")
elif caja_accesorio > caja_alimento and caja_accesorio > caja_juguete:
    print("La categoría con más ventas es: accesorio")
else:
    print("Hay un empate en las categorías con más ventas.")
    