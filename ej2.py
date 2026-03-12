print("Gym mazizo")

while True:
  try:
    edad = int(input("Ingrese su edad: "))
    if edad < 13:
        print("No puedes entrar al gimnasio, ingresa una edad valida.")

    elif 13 <= edad < 17:
        print("clase juvenil")

    elif 18 <= edad < 59:
        print("clase adulto")

    else:
        print("clase senior")

  except ValueError:
     print("Ingrese una edad valida para entrar al gimnasio.")