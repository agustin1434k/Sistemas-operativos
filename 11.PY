"""EJERCICIO 11"""
pares = 0
for _ in range(100):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
print(f"Cantidad de números pares: {pares}")
