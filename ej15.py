total = 0
carros = 0
motos = 0
max_pago = 0
placa_max = ""

for i in range(8):

    placa = input("Ingrese la placa del vehículo: ")
    tipo = input("Ingrese el tipo de vehículo (carro/moto): ").lower()
    horas = int(input("Ingrese el número de horas que el vehículo estuvo estacionado: "))

    if tipo == "carro":
        pago = 4000 * horas
        carros += 1
    elif tipo == "moto":
        pago = 2000 * horas
        motos += 1
    else:
        print("Tipo de vehículo no válido. Se considerará como carro.")
        pago = 4000 * horas
        carros += 1

    total += pago

    if pago > max_pago:
        max_pago = pago
        placa_max = placa
    print(f"El pago por el vehículo con placa {placa} es: {pago} pesos")
print(f"\n=== Resumen del estacionamiento ===")
print(f"Total recaudado: {total} pesos")
print(f"Cantidad de carros estacionados: {carros}")
print(f"Cantidad de motos estacionadas: {motos}")
print(f"El vehículo que pagó más es el de placa {placa_max} con un pago de {max_pago} pesos.")
