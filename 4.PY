"""EJERCICIO 4"""
n = int(input("Ingrese el número de términos: "))
suma = 0
for i in range(n):
    termino = 10 + i * 5
    suma += termino
print(f"Suma de la progresión: {suma}")