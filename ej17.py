total_dia = 0
contador_corte = 0
contador_cepillado = 0
contador_tintura = 0

for i in range(7):
    while True:
        nombre = input("Ingrese su nombre: ").lower()
        if nombre.isalpha():
            break
    while True:
        servicio_solicitado = input("Ingrese el servicio solicitado (corte, cepillado, tintura): ").lower()
        if servicio_solicitado in ["corte", "cepillado", "tintura"]:
            break
    while True:
        try:
            valor_pagado = float(input("Ingrese el valor pagado: "))
            if valor_pagado < 0:
                print("El valor no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    total_dia += valor_pagado

    if servicio_solicitado == "corte":
        contador_corte += 1
    elif servicio_solicitado == "cepillado":
        contador_cepillado += 1
    elif servicio_solicitado == "tintura":
        contador_tintura += 1

print("El total de ventas del día es: ", total_dia)
print("La cantidad de cortes realizados es: ", contador_corte)
print("La cantidad de cepillados realizados es: ", contador_cepillado)
print("La cantidad de tinturas realizadas es: ", contador_tintura)

if contador_corte > contador_cepillado and contador_corte > contador_tintura:
    print("El servicio más solicitado es: corte")
elif contador_cepillado > contador_corte and contador_cepillado > contador_tintura:
    print("El servicio más solicitado es: cepillado")
elif contador_tintura > contador_corte and contador_tintura > contador_cepillado:
    print("El servicio más solicitado es: tintura")
else:
    print("Hay un empate en los servicios más solicitados.")
