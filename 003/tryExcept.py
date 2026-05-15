# Uso y ejemplo s de while
# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except:
#         print("Solo numeros enteros")


# code=6767
# while True:
#     try:
#         pasw=int(input("Ingrese su clave: "))
#         if code==pasw:
#             print("Ingreso correcto")
#             break
#         else:
#             print("Clave Invalida")
#     except ValueError as er:
#         print("Solo numeros enteros")
#         print(er)

## tienda con manejo de error
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
#         match op:
#             case 1:
#                 print("El total a pagar es ",500000*1.19 )
#                 total+=500000*1.19
#             case 2:
#                 print("El total a pagar es ",450000*1.19 )
#                 total+=450000*1.19
#             case 3:
#                 print("El total a pagar es ",100000*1.19 )
#                 total+=100000*1.19
#             case 4:
#                 print("Saliendo")
#                 print("El total a pagar es", total)
#             case _:
#                 print("Opción inválida")
#     except ValueError as e:
#         print("Solo debe ingresar nuemros enteros. Error ",e)

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


