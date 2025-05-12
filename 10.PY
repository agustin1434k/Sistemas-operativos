"""EJERCICIO 10"""
contador_a = 0
for _ in range(50):
    caracter = input("Ingrese un carácter: ")
    if caracter == 'a':
        contador_a += 1
print(f"Cantidad de veces que se repite 'a': {contador_a}")