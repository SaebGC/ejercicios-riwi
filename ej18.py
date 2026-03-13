cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

total_promedios = 0
mejor_estudiante = ""
mejor_promedio = 0
contador_bajo = 0
contador_medio = 0
contador_alto = 0

for i in range(cantidad_estudiantes):
    print("Ingrese los datos del estudiante ", i + 1)

    nombre = input("Ingrese su nombre: ").lower()
    speaking = float(input("Ingrese nota de speaking: "))
    listening = float(input("Ingrese nota de listening: "))
    reading = float(input("Ingrese nota de reading: "))

    promedio = (speaking + listening + reading) / 3

    if promedio < 60: 
        print("el estudiante ", nombre, " tiene un promedio bajo.")

    elif promedio >= 60 and promedio <= 79:
        print("el estudiante ", nombre, " tiene un promedio medio.")

    else:
        print("el estudiante ", nombre, " tiene un promedio alto.")

    total_promedios += promedio

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre
    if promedio < 60:
        contador_bajo += 1
    elif promedio >= 60 and promedio <= 79:
        contador_medio += 1
    else:
        contador_alto += 1
print("El promedio general de la clase es: ", total_promedios / cantidad_estudiantes)
print("El estudiante con el mejor promedio es: ", mejor_estudiante, " con un promedio de: ", mejor_promedio)
print("La cantidad de estudiantes con promedio bajo es: ", contador_bajo)
print("La cantidad de estudiantes con promedio medio es: ", contador_medio)
print("La cantidad de estudiantes con promedio alto es: ", contador_alto)   
