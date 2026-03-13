bajo = 0
medio = 0
alto = 0

for i in range(5): 

 nombre = input("Ingrese su nombre: ")
 dias = int(input("Ingrese el número de días que ha asistido al gimnasio: "))
 minutos = int(input("Ingrese el número de minutos que ha pasado en el gimnasio: "))

 if dias < 3: 
    print(f"{nombre} tiene una asistencia baja.")
    bajo += 1
    
 elif dias >= 3 and dias <= 4:
        print(f"{nombre} tiene una asistencia media.")
        medio += 1
 else:
        print(f"{nombre} tiene una asistencia alta.")
        alto += 1


print(f"\n=== Resumen de asistencias ===")
print(f"Asistencia baja: {bajo}")
print(f"Asistencia media: {medio}")
print(f"Asistencia alta: {alto}")