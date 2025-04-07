"""ejercicio 1"""
print("calculator")
velocidad= int(input("ingrse la velocidad en m/s"))
t = int(input("velocidad en 5"))
distancia= (vel*t)
print("la distancia del calculo es de", dist)


"""ejercicio 2"""
nota1= int(input("la primer nota es"))
nota2= int(input("la segunda nota es"))
nota3= int(input("la tercera nota es"))
promedio=((nota1 + nota2+ nota3)/3)
print("el promedio es de", promedio)

"""ejercicio 3"""
ra= int(input("respuestas correctas"))
rb= int(input("respuestas incorrectas"))
rc= int(input("respuestas en blanco"))

ra = ra*3
rb = rb-1
rc = rc*3
pf= ra+rb+rc
print("el puntaje final es", pf)

"""ejercicio 4"""
re= int(input("partidos ganados"))
ru= int(input("partidos perdidos"))
rz= int(input("partidos emptados"))

re = re*3
ru = ru*0
rz = rz*1
pf= re+ru+rz
print("el puntaje final es", pf)

"""ejercicio 5"""
TAM= float(input("ingrese el tamaño de la copia"))
DISCO= 1.44
GB= 1024
DR= (GB/TAM)/DISCO
print(" se requieren", round(DR),"DISCO")
