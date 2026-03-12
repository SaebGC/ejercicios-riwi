cafe = 4000
te = 3500
jugo = 5000

while True:
    try:
        tipo_bebida = input("Ingrese el tipo de bebida (1.cafe, 2.te, 3.jugo): ")
        cantidad = int(input("Ingrese la cantidad de bebidas: "))   

        if tipo_bebida == "1":
            print(f"El precio del cafe es: {cafe} pesos")
            precio_unitario = 4000
        elif tipo_bebida == "2":
            print(f"El precio del te es: {te} pesos")
            precio_unitario = 3500    
        elif tipo_bebida == "3":
            print(f"El precio del jugo es: {jugo} pesos")
            precio_unitario = 5000
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 3.")

        precio_total = precio_unitario * cantidad 

        print(f"El precio total a pagar es: {precio_total} pesos")

    except ValueError:
        print("Ingrese una cantidad válida para calcular el precio total.")