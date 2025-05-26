Limite_presupuesto = 100000
total_gastos = 0

print("Ingresá tus gastos (0 para finalizar):")
gasto = int(input("Gasto: "))
while gasto != 0:
    total_gastos += gasto
    gasto = int(input("Gasto: "))

print("Total gastado:", total_gastos)
if total_gastos > Limite_presupuesto:
    print("¡Atención! Superaste el límite presupuestado.")