servicio = input("Ingrese el servicio a pedir (1. masaje 2.facial 3.manicure): ").lower()

if servicio == "masaje" or servicio == "1":
    print("Has seleccionado masaje")

elif servicio == "facial" or servicio == "2":
    print("Has seleccionado facial")

elif servicio == "manicure" or servicio == "3":
    print("Has seleccionado manicure")

else:
    print("Aun no contamos con otro servicio.")