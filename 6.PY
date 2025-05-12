"""EJERCICIO 6"""
num = int(input("Ingrese un número entero positivo: "))
invertido = 0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10
print(f"Número invertido: {invertido}")