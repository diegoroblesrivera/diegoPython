











# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except:
#         print("Solo numeros enteros")
    




# while True:
#     n=input("Ingrese su nombre")
    
# op=0
# total=0
# while op!=4:
#     try:
#         print("1.- Xbox Series S $250.000")
#         print("2.- Sony PS5 $ $500.000")
#         print("3.- LGTV 60 Pulgadas $600.000")
#         print("4.- Salir")
#         op=int(input("Seleccione una opcion: "))
#     except:
#         print("SOLO SE ACEPTAN NUMEROS ENTEROS")
#     match op:
#         case 1:
#             print("El valor a pagar ", 250000*1.19)
#             total+=250000*1.19
#         case 2:
#             print("El valor a pagar ", 500000*1.19)
#             total+=500000*1.19
#         case 3:
#             print("El valor a pagar ", 600000*1.19)
#             total+=600000*1.19
#         case 4:
#             print("Saliendo")
#             print(f"El total a pagar es {total}")
#         case _:
#             print("Opcion Invalida")

# while True:
#     try:
#         notas=int(input("Ingrese la cant de notas: ")) # aqui
#         break
#     except:
#         print("Ingresar solo numeros enteros")


# suma=0
# for i in range(notas):
#     while True:
#         try:
#             n=float(input(f"Ingrese la nota {i+1}: ")) #acá
#             if 1<=n<=7:
#                 break
#             else:
#                 print("Nota fuera de rango, (1.0-7.0)")
#         except:
#             print("Ingresar solo numeros enteros")
    
#     suma=suma+n
#     # suma+=n
# prom=suma/notas
# print("El promedio es",round(prom,1) )

# if prom>=4:
#     print("Alumno aprobado")
# else:
#     print("Alumno reprobado")

# Deberás construir un programa que esta diseñado para ayudar en la venta
#  de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego,
#  utiliza un proceso organizado (llamado bucle for) para pedirte el precio
#  de cada pasaje por separado. Si ingresas un valor que no es un número, 
# te in-dica que necesitas proporcionar un valor numérico válido. Al final,
#  muestra el monto total que se ha obtenido por la venta de todos los pasajes
# •	Solicita al usuario la cantidad de pasajes a vender.
# •	Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
# •	Dentro del bucle, se solicita al usuario el precio de cada pasaje y 
# se acumula en la variable totalIngresos.
# •	Si el usuario ingresa un valor no numérico para el precio del pasaje, 
# el programa muestra un mensaje y sale del bucle usando break.
# •	Finalmente, se imprime el total de ingresos por la venta de pasajes
while True:
    try:
        num=int(input("Ingrese la cantidad de pasajes a vender: "))
        break
    except:
        print("Solo numeros enteros")
totalIngresos=0
for i in range(num):
    while True:
        try:
            precio=int(input(f"Ingrese el precio del pasaje {i+1}: "))
            totalIngresos+=precio
            break
        except ValueError as e:
            print("Solo numeros enteros.Error: ", e)
            
print("El total a pagar es ",totalIngresos)



