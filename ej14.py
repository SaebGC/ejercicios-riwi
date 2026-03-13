total = 0
niños = 0
adultos = 0
ancianos = 0

capacidad = int(input("Ingrese la capacidad máxima del cine: "))
 
while True:

    edad = int(input("Ingrese su edad: "))

    if edad <=17:
        print("Niño")
        niños += 1
    elif edad >= 18 and edad < 65:
        print("Adulto")
        adultos += 1
    else:
        print("Anciano")
        ancianos += 1
    total += 1
    if total >= capacidad:
        print("El cine ha alcanzado su capacidad máxima. No se permiten más entradas.")
        break

print(f"Total de niños: {niños}")
print(f"Total de adultos: {adultos}")
print(f"Total de ancianos: {ancianos}")
print(f"Total de personas en el cine: {total}")
if total == capacidad:
        print("La sala del cine se ha llenado")
else:
     print("La sala del cine no se ha llenado") 