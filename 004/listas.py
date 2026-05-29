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

productos=[
   ["Xbox Series S", 300000],
   ["Sony PS5", 600000],
   ["LGTV 60 Pulgadas", 450000]
]

def menuProd():
   select=1
   for p in productos:
      print(f"{select}.- Producto: {p[0]} Precio: $ {p[1]}")
      select+=1

def menuPrincipal():
   print("1.- Menu admin")
   print("2.- Menu cliente")
   print("3.- Salir")

op=0


def selectProd():
   total=0
   while True:
      menuProd()
      print("4.- Salir")
      op=int(input("Seleccione una opcion: "))
      match op:
         case 1:
               print("El valor a pagar ", 250000*1.19)
               total+=250000*1.19
         case 2:
               print("El valor a pagar ", 500000*1.19)
               total+=500000*1.19
         case 3:
               print("El valor a pagar ", 600000*1.19)
               total+=600000*1.19
         case 4:
               print("Saliendo")
               print(f"El total a pagar es {total}")
               break
         case _:
               print("Opcion Invalida")

def selectAdmin():
    while True:
      print("1.- Agregar Producto")
      print("2.- Eliminar Producto")
      print("3.- Actualizar Producto")
      print("4.- Mostrar Productos")
      print("5.- Volver al menu principal")
      op=int(input("Seleccione una opcion: "))
      match op:
         case 1:
            nombreP=input("Ingrese el nombre del Producto: ")
            precioP=int(input("Ingrese el precio del Producto: "))
            productos.append([nombreP, precioP])
         case 4:
            menuProd()
         case 5:
            print("Salir")
            break
         case _:
            print("Opcion invalida")   

def selectPrin():
   while True:
      menuPrincipal()
      op=int(input("Seleccione una opcion: "))
      match op:
         case 1:
            print("---Menu admin---")
            selectAdmin()
         case 2:
            print("---Menu Cliente---")
            selectProd()
         case 3:
            print("Salir")
            break
         case _:
            print("Opcion invalida")   
  
selectPrin()         


