"""ejercicio 1"""
edad = int(input("ingrese su edad: "))

if edad < 18:
    print("categoria: menor de edad")
elif 18 <= edad <= 64:
    print("categoria: adulto")
else: 
    print("categoria: adulto mayor")


"""ejercicio 2"""
velocidad = int(input("ingrese la velocidad del vehiculo (km/h): ")) 

if velocidad <= 60:
    print("esta dentro del limite permitido. ")
elif 61 <= velocidad <=80:
    print("esta en exceso leve de velocidad. ")
else: 
    print("esta en exceso grave de velociudad. ")


"""ejercicio 3"""
opcion = int(input("elija una opcion:/n1. hamburguesa/n2. pizza/n3. ensalada/n4. salir/n"))

match opcion:
    case 1: 
        print("eligio: hamburguesa")
    case 2:
        print("eligio pizza")
    case 3:
        print("eligio ensalada")
    case 4:
        print("saliendo del programa...")
    case _:
        print("opcion invalida")


"""ejercicio 4"""
saldo = float(input("ingrese su saldo actual: "))
retiro = float(input("ingrese el monto a retirar: "))

if retiro <= saldo:
    saldo _= retiro
    print(f"operacion exitosa. saldo restante: ${saldo: .2f}")
else:
    print("fondos insuficientes.")    


"""ejercicio 5"""
dia = int(input("ingrese un numero de dia(1=lunes, 7=domingo): "))

if 1 <= dia <= 5:
    print("es un dia laboral.")
elif dia == 6 or dia == 7:
    print(" es fin de semana. ")
else:
    print("numero de dia invalido. ")        