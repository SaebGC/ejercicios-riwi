total_venta = 0
clientes = 0
cono = 0
vaso = 0
banana_split = 0

while True:
 pedidos = input("seleccione el tipo de pedido (cono, vaso, banana_split): ").lower()
 cantidad = int(input("Ingrese la cantidad de pedidos: "))
 if pedidos == "cono":
        cono += 1
        total_venta += 3000 * cantidad

 elif pedidos == "vaso":
        vaso += 1
        total_venta += 4000 * cantidad
 elif pedidos == "banana_split":
        banana_split += 1
        total_venta += 9000 * cantidad
 else:
     print("Tipo de pedido no válido. Por favor, seleccione nuevamente.")
 continuar = input("Quiere seguir con otro pedido? (s/n): ").lower()
 clientes += 1 
 if continuar != "s":
    break

print(f"\n=== Resumen de ventas ===")
print(f"Total de ventas: {total_venta} pesos")
print(f"Total de clientes atendidos: {clientes}")
print(f"Cantidad de pedidos de cono: {cono}")
print(f"Cantidad de pedidos de vaso: {vaso}")
print(f"Cantidad de pedidos de banana split: {banana_split}")

if cono > vaso and cono > banana_split:
    print("El producto más vendido es el cono.")

elif vaso > cono and vaso > banana_split:
    print("El producto más vendido es el vaso.")

elif banana_split > cono and banana_split > vaso:
    print("El producto más vendido es el banana split.")

else:
     print("No hay productos más vendidos, hay un empate entre dos o más productos.")