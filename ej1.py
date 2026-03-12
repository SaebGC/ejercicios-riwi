print("Heladeria L bay ")

vainilla = 0
chocolate = 0
fresa = 0
pedidos = 0


while pedidos < 5: 
    print(f"\n---Cliente {pedidos + 1} de 5---")
    print("1.vainilla")
    print("2.chocolate")
    print("3.fresa")

    opcion = input("Seleccione un sabor: ")

    if opcion == "1":
        print("Has seleccionado vainilla")
        vainilla += 1
        pedidos += 1
    elif opcion == "2":
        print("Has seleccionado chocolate")
        chocolate += 1
        pedidos += 1
    elif opcion == "3":
        print("Has seleccionado fresa")
        fresa += 1
        pedidos += 1
    else:
        print("Opción no válida, por favor seleccione una opción del 1 al 3.")

print(f"\n=== Resumen de pedidos ===")
print(f"Vainilla: {vainilla} veces")
print(f"Chocolate: {chocolate} veces")
print(f"Fresa: {fresa} veces")