# EXPLICACION Y USO DE LISTAS

lista=[8, 20, 12, 87, 1024]
#      0  1    2  3     4
       
# print(lista)
# print(lista[4])

# for k in lista:
#     print("Numero: ",k)

# Crear una lista de 4 frutas 
# mostrar cada elemento individualmente



# frutas=["Uva", "Mango", "Pera", "Kiwi", "anana"]

# frutas.append("Higo")
# frutas.append("Frutilla")

# print(frutas[3][2])
# vocales="aeiou"
# for f in frutas:
#     if f[0].lower() in vocales:
#         print(f"La fruta {f} comienza con vocal")
#     else:    
#         print(f"La fruta {f} NO comienza con vocal")

# Hacer una lista de  3 nombres y otra de  3 apellidos
# mostrar las listas como si fueran nombre
# vale decir, Diego Robles, Adolfo Hinako, Luis Mussolini.

# ##Ejemplo de lisas entrelazadas
# nombres=["Curly", "Larry", "Moe", "Joe"]
# ape=["Montana", "Montaño", "Manzanero", "Pino"]
    
# for n in range(len(nombres)):
#     print(nombres[n], ape[n])

# # La listas puede tener tipos de datos dispares 
# datos=[4, 6.9, "Alonsonic", False]

# for d in datos:
#     print(d)

# matrix=[
#     [5,8,3], [79, "LINK", 24]
# ]
# print(matrix)
# print(matrix[1])
# print(matrix[1][0])


''' 
Modificar el programa del carrito de comprar
para poder utilizarlo con listas
EL producto debe tener Nombre y precio
'''

# productos=[]
# while True:
#     print("1.- Agregar Producto")
#     print("2.- Mostrar Productos")
#     print("3.- Eliminar Producto")
#     print("4.- Salir")
#     op=int(input("Seleccione una opcion"))
#     match op:
#         case 1:
#             nombre=input("Ingrese el nombre del producto: ")
#             precio=int(input("Ingrese el precio del producto: "))
#             nuevo_producto={"nombre":nombre, "precio":precio}
#             productos.append(nuevo_producto)
#         case 2:
#             print(productos)
#         case 3:
#             print("")
#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("Opcion invalida")

# colores=["blanco", "negro", "purpura", "naranja"]

# for c in colores:
#     print(c)

# agregar=input("Ingrese un color: ")

# colores.append(agregar)

# for c in colores:
#     print(c)


juguetes=["yo-yo", "tetris"]

def mostrarJuguetes():
    for j in range(len(juguetes)):
        print(f"{j+1}.- {juguetes[j]}")
def mostrarJ():
    print("-"*20)
    c=1
    for i in juguetes:
        print(f"{c}.- {i}")
        c+=1
def agrgegar():
    print("-"*20)
    agregar=input("Ingrese un juguete: ")
    juguetes.append(agregar)
def eliminar():
    print("-"*20)
    mostrarJ()
    eliminar=int(input("Que jueguete desea eliminar?: "))
    juguetes.pop(eliminar-1)
    print(f"{juguetes[eliminar-1]} fue eliminado correctamente")
def actualizar():
    print("-"*20)
    mostrarJ()
    actualizar=int(input("Que jueguete desea actualizar?: "))
    juguetes[actualizar-1]=input("Ingrese el nuevo nombre: ")
    print("Actualizado con exito")

def menuListaJ():    
    while True:
        try:
            print("-"*20)
            print("1.- Agregar Juguete")
            print("2.- Eliminar Juguete")
            print("3.- Actualizar Juguete")
            print("4.- Mostar Juguetes")
            print("5.- Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agrgegar()
                case 2:
                    eliminar()
                case 3:
                    actualizar()
                case 4:
                    mostrarJ()
                case 5:
                    print("Saliendo")
                    break
                case _:
                    print("Opcion invalida")
        except:
            print("Solo numeros enteros")


menuListaJ()

