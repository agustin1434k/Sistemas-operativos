aprobados = 0
desaprobados = 0

for i in range(1, 11):
    nota = int(input(f"nota del alumno{i}: "))
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print("aprobaron:", aprobados)
print("desaprobaeon:", desaprobados)