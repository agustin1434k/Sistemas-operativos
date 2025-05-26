limite_diario = 20000
total = 0

print("ingresa los montos de tus compras: ")
compra = float(input("compra: "))
while total + compra <=
limite_diario and compra = 0:
  total += compra
  print(F"total acumulado:{total}")
  compra = float(input("compra"))

if total + compra > limite_diario:
    print("no podes seguir comprando" and "superaste el limitee diario.")
print("total gastado en el dia:", total)