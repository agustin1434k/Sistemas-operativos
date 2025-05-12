"""EJERCICIO 9"""
n = int(input("¿Cuántos números va a ingresar?: "))
mayor = None
menor = None
for _ in range(n):
    num = int(input("Ingrese un número: "))
    if mayor is None or num > mayor:
        mayor = num
    if menor is None or num < menor:
        menor = num
print(f"Mayor: {mayor}, Menor: {menor}")