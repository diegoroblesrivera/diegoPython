# while True:
#     try:
#         edad=int(input("Ingrese su edad: ")) # si aparece un error, 
#         # salta a la linea 6, donde esta except para manejar el error
#         print("Su edad es", edad)
#         break
#     except ValueError as valordelError:
#         print("Solo se aceptan numeros enteros")
#         print(valordelError)

# edad=int(input("Ingrese su edad: "))


# for i in range(10):
#     n1=int(input("Ingrese un numero: "))
#     if n1%2!=0:
#         break

# ingrese nuemros indefinidamente 
# hasta que ponga el numero 0.
# Sumelos y muestre el total. 
# num=0
# while True:
#     try:
#         n1=int(input("Ingrese un numero: "))
#         num+=n1
#         if n1==0:
#             break
#     except:
#         print("SOlo numeros enteros")

# print("EL total es" , num)

## Ejempo de menu con 
# try except

# op=0
# total=0
# cantPRod=0
# while op!=4:
#     try:
#         print("1.- Radio sterero Sony $70.000")
#         print("2.- LGTV 55 pulgadas Super gamer $500.000 ")
#         print("3.- PS5 $580.000")
#         print("4.- Salir")
#         print("Seleccione una opcion")
#         op=int(input())

#         match op:
#             case 1:
#                 print("El precio a pagar es ", 70000*1.19)
#                 total+=70000*1.19
#                 cantPRod+=1
#             case 2:
#                 print("El precio a pagar es ", 500000*1.19)
#                 total+=500000*1.19
#                 cantPRod+=1
#             case 3:
#                 print("El precio a pagar es ", 580000*1.19)
#                 total+=580000*1.19
#                 cantPRod+=1
#             case 4:
#                 print(f"Su total a pagar es {total}")
#                 print(f"La cantidad de articulos es {cantPRod}")
#             case _:
#                 print("Opcion Inválida")  # opcion por defecto
#     except :
#         print("Debe ingresar solo numeros enteros")

porc=float(input("Ingrese el porcetaje de rucos en su comuna"))

if porc>0 and porc<100:
    print("Porcentaje correcto")
else:
    print("Porcentaje fuera de rango")



