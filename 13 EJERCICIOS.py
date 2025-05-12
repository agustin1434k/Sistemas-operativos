"""EJERCICIO 1"""
pares = 0
for _ in range(100):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
print(f"Cantidad de números pares: {pares}")


"""EJERCICIO 2"""
print("Número - Cubo")
for i in range(1, 11):
    par = i * 2
    cubo = par ** 3
    print(f"{par} - {cubo}")

"""EJERCICIO 3"""
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

contador = 0
numero = 2
print("Primo - Cubo")
while contador < 10:
    if es_primo(numero):
        print(f"{numero} - {numero**3}")
        contador += 1
    numero += 1

"""EJERCICIO 4"""
n = int(input("Ingrese el número de términos: "))
suma = 0
for i in range(n):
    termino = 10 + i * 5
    suma += termino
print(f"Suma de la progresión: {suma}")

"""EJERCICIO 5"""
n = int(input("Ingrese el valor de N: "))
suma = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        suma -= 1 / i
    else:
        suma += 1 / i

print(f"El resultado de la serie es: {suma}")

"""EJERCICIO 6"""
num = int(input("Ingrese un número entero positivo: "))
invertido = 0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10
print(f"Número invertido: {invertido}")

"""EJERCICIO 7"""
num = int(input("Ingrese un número: "))
if es_primo(num):
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")

"""EJERCICIO 8"""
cantidad = int(input("¿Cuántos números va a ingresar?: "))
ceros = 0
for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num == 0:
        ceros += 1
print(f"Cantidad de ceros ingresados: {ceros}")

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

"""EJERCICIO 10"""
contador_a = 0
for _ in range(50):
    caracter = input("Ingrese un carácter: ")
    if caracter == 'a':
        contador_a += 1
print(f"Cantidad de veces que se repite 'a': {contador_a}")

"""EJERCICIO 11"""
pares = 0
for _ in range(100):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
print(f"Cantidad de números pares: {pares}")

"""EJERCICIO 12"""
print("Número - Cubo")
for i in range(1, 11):
    par = i * 2
    cubo = par ** 3
    print(f"{par} - {cubo}")

"""EJERCICIO 13"""
n = int(input("Ingrese la cantidad de empleados: "))
mayor_sueldo = 0
orden_mayor = 0
for i in range(1, n + 1):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i}: "))
    if sueldo > mayor_sueldo:
        mayor_sueldo = sueldo
        orden_mayor = i
print(f"Empleado con mayor sueldo: {orden_mayor} - Sueldo: {mayor_sueldo}")
