
while True:
 try:
    hora = int(input("Ingrese la hora en formato 24 horas: "))

    if hora >= 6 and hora < 11:
        print("Turno mañana")

    elif hora >= 12 and hora < 17:
        print("Turno tarde")

    elif hora >= 18 and hora < 22:
        print("Turno noche")

    else:
        print("Hora inexistente de horario")

 except ValueError:
        print("Ingrese una hora valida para determinar el turno.")