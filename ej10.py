clases = int(input("Ingrese el número de clases asistidas: "))

if clases < 5:
    print("Asistencia baja")

elif 5 <= clases <=8:
    print("Asistencia media")


else:
    print("Asistencia alta")