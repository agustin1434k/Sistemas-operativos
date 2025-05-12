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