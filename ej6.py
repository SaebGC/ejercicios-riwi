parqueo = int(input("Ingrese cuantas horas estuvo parqueado: "))

if parqueo <= 1:
        print("El precio a pagar es: 5000 pesos")

elif parqueo > 1 :
        precio = 5000 + (parqueo - 1) * 3000
        print(f"El precio a pagar es: {precio} pesos")

