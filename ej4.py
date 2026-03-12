while True:
    try:
        edad = int(input("Ingrese su edad: "))

        if edad < 12:
            print("precio por entrada: 8000 pesos")
        elif edad >= 12 and edad <= 59:
            print("precio por entrada: 12000 pesos")
        else:
            print("precio por entrada: 9000 pesos")

    except ValueError:
        print("Ingrese una edad valida para calcular el precio de la entrada.")