# explicacion y uso de FOR

# for i in range(5):
#     print(i+1)

# num=int(input("Ingrese un numero"))
# for i in range(1,num+1):
#     print("Repeticion", i)

# for i in range(num):
#     print("Repeticion", i+1)

# # pedir un numero al usuario y mostrar
# # su tabla de multiplicar

# num=int(input("Ingrese un numero"))

# for i in range(1,11):
#     print(f"{num}x{1}={num*i}")

# Pedir al usuario la cantidad d notas 
# mostrar el premedio de ellas
# determinar si el alumno aprueba o no

# notas=int(input("Ingrese la cant de notas: "))
# suma=0
# for i in range(notas):
#     n=float(input(f"Ingrese la nota {i+1}: "))
#     suma=suma+n
#     # suma+=n
# prom=suma/notas
# print("El promedio es",round(prom,1) )

# if prom>=4:
#     print("Alumno aprobado")
# else:
#     print("Alumno reprobado")

# #sumatoria


# num=int(input("Ingrese un numero: "))
# total=0
# for i in range(num):
#     total=total+i+1
# print(f"El resultado es {total}")


#Factorial

num=int(input("Ingrese un numero: "))
total=1
for i in range(num):
    total=total*(i+1)
print(f"El resultado es {total}")


