# # Ejemplo y yuso de listas

# #     -5  -4 -3 -2 -1
# lista=[4, 7, 9, 2, 3.8]
# #      0  1  2  3  4

# print(lista)
# print(lista[-4])

# name="LINK"

# # for i in name:
# #     print(i)

# for i in lista:
#     print(i)

# Cree una lista de 4 frutas y muestrelas por pantalla

# frutas=["Uva", "pera", "Sandia", "Piña", "anana" ]
# ccVocal=0
# for f in frutas:
#     if f[0].lower() in ("aeiou"):
#         print("La fruta es ", f, " comienza con vocal")
#         ccVocal+=1
#     else:
#         print("La fruta es ", f)
# print("Total de frutas que inician con vocal: ", ccVocal)


# Cree una lista con 3 nombres
# Cree otra lista con 3 apellidos
# Muestre ambos por pantalla

# nombres=["Pedro", "Juan", "Diego", "Donald"]
# ape=["Pascal", "Segovia", "Robles", "Pent"]

# for p in range(len(ape)):
#     print(nombres[p], ape[p])

# nombres.append("Felipe")
# ape.append("Camiroaga")

# for p in range(len(ape)):
#     print(nombres[p], ape[p])

# crea una lista de animales con 3 elementos
# Agregue 2 mas
# y muestre el resultado de la misma

# animales=["Dragon", "Lamprea", "Ñu"]

# animales.append("Hiena")
# animales.append("Huron")

# for a in animales:
#     print(a)

# productos=[
#    ["Xbox Series S", 300000],
#    ["Sony PS5", 600000],
#    ["LGTV 60 Pulgadas", 450000]
# ]

# def menuProd():
#    select=1
#    for p in productos:
#       print(f"{select}.- Producto: {p[0]} Precio: $ {p[1]}")
#       select+=1

# def menuPrincipal():
#    print("1.- Menu admin")
#    print("2.- Menu cliente")
#    print("3.- Salir")

# op=0


# def selectProd():
#    total=0
#    while True:
#       menuProd()
#       print("4.- Salir")
#       op=int(input("Seleccione una opcion: "))
#       match op:
#          case 1:
#                print("El valor a pagar ", 250000*1.19)
#                total+=250000*1.19
#          case 2:
#                print("El valor a pagar ", 500000*1.19)
#                total+=500000*1.19
#          case 3:
#                print("El valor a pagar ", 600000*1.19)
#                total+=600000*1.19
#          case 4:
#                print("Saliendo")
#                print(f"El total a pagar es {total}")
#                break
#          case _:
#                print("Opcion Invalida")

# def selectAdmin():
#     while True:
#       print("1.- Agregar Producto")
#       print("2.- Eliminar Producto")
#       print("3.- Actualizar Producto")
#       print("4.- Mostrar Productos")
#       print("5.- Volver al menu principal")
#       op=int(input("Seleccione una opcion: "))
#       match op:
#          case 1:
#             nombreP=input("Ingrese el nombre del Producto: ")
#             precioP=int(input("Ingrese el precio del Producto: "))
#             productos.append([nombreP, precioP])
#          case 4:
#             menuProd()
#          case 5:
#             print("Salir")
#             break
#          case _:
#             print("Opcion invalida")   

# def selectPrin():
#    while True:
#       menuPrincipal()
#       op=int(input("Seleccione una opcion: "))
#       match op:
#          case 1:
#             print("---Menu admin---")
#             selectAdmin()
#          case 2:
#             print("---Menu Cliente---")
#             selectProd()
#          case 3:
#             print("Salir")
#             break
#          case _:
#             print("Opcion invalida")   
  
# selectPrin()         


# # Crear una lista de 7 numeros no sucesivos
# # mostrar el menor  y mayor de ellos 

# nums=[15, 20, 67, 27, 420, 7, 12, -6, 555]

# print(nums)
# nums.sort()
# print(nums)
# print(f"El numero mayor es {nums[-1]}")
# print(f"El numero menor es {nums[0]}")
# nums.reverse()
# print(nums)

# Crear una lista de productos con nombre y precio
# odenar por precio de menor a mayor

prods=[
    ["pendrive", 8000],
    ["HDMI 2.1", 13000],
    ["Disco duro 1 TB", 35000],
    ["Teclado", 15000]
]
# for p in prods:
#     print(p[0], "= $", p[1])
# prods.sort(key=lambda p:p[1])
# for p in prods:
#     print(p[0], "= $", p[1])
# Sumar el precio de todos los productos
# print(prods[2])
# total=0
# for p in prods:
#    total=total+p[1]

# print("El total de los productos es", total)

notas=[4.6, 6.8, 4.1]
def muestraNotas():
   print("-"*30)
   c=1
   for f in notas:
      print(f"{c}.- {f}")
      c+=1
   print("-"*30)
def agregaNotas():
   n=float(input("Ingrese la nota: "))
   notas.append(n)
   print("Agregado correctamente")
def promedioNotas():
   suma=0
   for n in notas:
      suma=suma+n
   prom=suma/len(notas)
   print(f"El promedio es {round(prom, 1)}")
'''Ejercicio	Completar con las sentencias de código, que permitan realizar: 
1.- Agregar notas a la lista creada
2.- Muestre por pantalla todas las notas ingresadas
3.- Muestra la cantidad de notas ingresadas
4.- Obtenga el promedio de las notas'''

def menuNotas():
   while True:
      try:
         print('''
   1.- Agregar notas a la lista creada
   2.- Muestre por pantalla todas las notas ingresadas
   3.- Muestra la cantidad de notas ingresadas
   4.- Obtenga el promedio de las notas
   5.- Salir''')

         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregaNotas()
               case 2:
                  muestraNotas()
               case 3:
                  print(f"La cantidad de notas son {len(notas)}")
               case 4:
                  promedioNotas()
               case 5:
                  print("Saliendo")
                  break
               case _:
                  print("Opcion invalida")

      except ValueError as e:
         print("Error" , e)

menuNotas()
