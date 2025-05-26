total_vasos = 0

for dia in range(1, 8):
    vasos = int(input(f"vasos de agua en el dia{dia}"))
    total_vasos += vasos

promedio = total_vasos/7
print("promedio diario de agua:", promedio)

if promedio < 8:
    print("aumento el cosnumo de agua.")