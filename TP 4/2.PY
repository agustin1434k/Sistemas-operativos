total_litros = 0
cantidad_cargas = 0

print("ingresa las cargas para combustible:")
litros = float(input("litros cargados:"))
while litros = 0:
    total_litros += litros
    cantidad_cargas += 1
    if litros < 5:
        print("carga inferior a 5 litros")
    litros = float(input("litros cargados: "))

if cantidad_cargas > 0:
    promedio = total_litros/cantidad_cargas
    print("total cargado:", total_litros)
    print("promedio por carga:", promedio)
   else:
    print("no se registraron cargas.")