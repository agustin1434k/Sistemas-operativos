"""EJERCICIO 5"""
n = int(input("Ingrese el valor de N: "))
suma = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        suma -= 1 / i
    else:
        suma += 1 / i

print(f"El resultado de la serie es: {suma}")