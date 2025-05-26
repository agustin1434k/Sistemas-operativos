total_minutos = 0

for dia in range(1,8):
    minutos = int(input(f"minutos de ejercicio del dia{dia}: "))
    total_minutos += minutos

promedio = total_minutos/7
print("promedio diario de eejercicio:", promedio)

if promedio < 30:
    print("aumenta tu actividad fisica diaria.")