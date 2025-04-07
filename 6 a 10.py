"""ejercicio 6"""
ay=float(input("ingrese el valor de y de a"))
ax=float(input("ingrese de x de a"))
by=float(input("ingrese el valor de y de b"))
bx=float(input("ingrese de x de b"))
dist=round.(((((ay-by)**2)+((ax-bx)**2))**0,5),2)
print("la distancia entre a y b es de", dist)

"""ejercicio 7"""
num1= int(input("ingrese el primer numero"))
num2= int(input("ingrese el segundo numero"))
promedio=(num1+num2)/2

"""ejercicio 8"""
print("perimetro de un rectangulo")
l1=float(input("el valor del primer lado"))
l2=float(input("el valor del segundo lado"))
perimetro=(l1*2+l2*2)
area=(l1*l2)
print("el perimetro del rectangulo es", perimetro)
print("el area del rectangulo es", area)

"""ejercicio 9"""
GL=3.785
PRECIO= 1.200
CT=float(input("galones surtidos: "))
L= CT*GL
PT= L*PRECIO
print("el total a pagar es de", PT)

"""ejercicio 10"""
R=float(input("ingrese el radio: "))
A=float(input("ingese el alto: "))
PL= 3.1416
V=PL * (r*2)*A
ARE= 2*PL*R*A
print("el volumen es de: ",V)
print("y el area es de:", ARE)