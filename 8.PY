"""EJERCICIO 8"""
cantidad = int(input("¿Cuántos números va a ingresar?: "))
ceros = 0
for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num == 0:
        ceros += 1
print(f"Cantidad de ceros ingresados: {ceros}")