# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
        
#     except ValueError as er:
#         print("Error", er)
#         print("Solo debe ingresar numeros enteros")
#     else:
#         print("Numero ingresado correctamente")
#         break


# op=0
# total=0
# while op!=4:
#     try:
#         print("1.- PC $500.000")
#         print("2.- LGTV 55 pulgadas $450.000")
#         print("3.- Microondas Mademsa $100.000")
#         print("4.- Salir")
#         print("Seleccione una opcion")
#         op=int(input())
#     except ValueError as e:
#         print("Error", e)
#         print("Solo se aceptan numeros enteros")
#     match op:
#         case 1:
#             print("El total a pagar es ",500000*1.19 )
#             total+=500000*1.19
#         case 2:
#             print("El total a pagar es ",450000*1.19 )
#             total+=450000*1.19
#         case 3:
#             print("El total a pagar es ",100000*1.19 )
#             total+=100000*1.19
#         case 4:
#             print("Saliendo")
#             print("El total a pagar es", total)
#         case _:
#             print("Opción inválida")
# while True:
#     try:
#         notas=int(input("Ingrese la cant de notas: "))
#         break
#     except:
#         print("Solo mnumeros enteros")

# suma=0
# for i in range(notas):
#     while True:
#         try:
#             n=float(input(f"Ingrese la nota {i+1}: "))
#             break
#         except ValueError:
#             print("Solo numeros decimales")
#     suma=suma+n
#     # suma+=n
# prom=suma/notas
# print("El promedio es",round(prom,1) )

# if prom>=4:
#     print("Alumno aprobado")
# else:
#     print("Alumno reprobado")


# actividad 2.4.3


# Deberás construir un programa que esta diseñado para ayudar en la venta de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego, utiliza un proceso organizado (llamado bucle for) para pedirte el precio de cada pasaje por separado. Si ingresas un valor que no es un número, te indica que necesitas proporcionar un valor numérico válido. Al final, muestra el monto total que se ha obtenido por la venta de todos los pasajes
# •	Solicita al usuario la cantidad de pasajes a vender.
# •	Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
# •	Dentro del bucle, se solicita al usuario el precio de cada pasaje y se acumula en la variable totalIngresos.
# •	Si el usuario ingresa un valor no numérico para el precio del pasaje, el programa muestra un mensaje y sale del bucle usando break.
# •	Finalmente, se imprime el total de ingresos por la venta de pasajes




while True:
    try:
        pas=int(input("Cuantos pasajes desea llevar: "))
        break
    except ValueError as e:
        print("Error", e)
        print("Solo numeros enteros")
total=0
for i in range(pas):
    while True:
        try:
            precio=int(input(f"Cuanto vale el pasaje {i+1}: "))
            break
        except ValueError as a:
            print("Error", a)
            print("Solo numeros enteros")
    total+=precio
print(f"El precio total a pagar es de {total}")
