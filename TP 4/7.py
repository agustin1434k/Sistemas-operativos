total_temperatura = 0
dias_calidos = 0

for dia in range(1,8):
    temp = float(input(f"temperatura maxima del dia{dia}: "))
    total_temperatura += temp
    if temp > 30:
        dias_calidos += 1

media = total_temperatura/7
print("temperatura media semanal.", media)
print("dias con mas de 30°c:", dias_calidos)