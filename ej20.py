cantidad_usuarios = int(input("Ingrese la cantidad de usuarios: "))

total_recaudacion = 0
contador_basico = 0
contador_premium = 0
contador_familiar = 0
for i in range(cantidad_usuarios):
    nombre = input("Ingrese su nombre: ").lower()
    edad = int(input("Ingrese su edad: "))
    tipo_plan = input("Ingrese el tipo de plan (basico, premium, familiar): ").lower()

    if tipo_plan == "básico":
        total_recaudacion += 50000
        contador_basico += 1
    elif tipo_plan == "premium":
        total_recaudacion += 90000
        contador_premium += 1
    elif tipo_plan == "familiar":
        total_recaudacion += 130000
        contador_familiar += 1
    else:
        print("Tipo de plan no válido.")

    if edad < 18: 
        print("El cliente ", nombre, " registro juvenil")
    elif edad >= 60:
        print("El cliente ", nombre, " beneficio senior")

print("La recaudación total es: ", total_recaudacion)
print("La cantidad de usuarios con plan básico es: ", contador_basico)
print("La cantidad de usuarios con plan premium es: ", contador_premium)
print("La cantidad de usuarios con plan familiar es: ", contador_familiar)
if contador_basico > contador_premium and contador_basico > contador_familiar:
    print("El plan más popular es: básico")
elif contador_premium > contador_basico and contador_premium > contador_familiar:
    print("El plan más popular es: premium")
elif contador_familiar > contador_basico and contador_familiar > contador_premium:
    print("El plan más popular es: familiar")    
else:    
    print("Hay un empate en los planes más populares.")