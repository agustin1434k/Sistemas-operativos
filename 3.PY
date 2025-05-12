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

