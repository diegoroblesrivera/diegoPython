# eXPLICACION U USO DE LISTAS

lista=[8, 20, 12, 87, 1024]
#      0  1    2  3     4
       
# print(lista)
# print(lista[4])

# for k in lista:
#     print("Numero: ",k)

# Crear una lista de 4 frutas 
# mostrar cada elemento individualmente



frutas=["Uva", "Mango", "Pera", "Kiwi", "anana"]

frutas.append("Higo")
frutas.append("Frutilla")

print(frutas[3][2])
vocales="aeiou"
for f in frutas:
    if f[0].lower() in vocales:
        print(f"La fruta {f} comienza con vocal")
    else:    
        print(f"La fruta {f} NO comienza con vocal")

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

productos=[]
while True:
    print("1.- Agregar Producto")
    print("2.- Mostrar Productos")
    print("3.- Eliminar Producto")
    print("4.- Salir")
    op=int(input("Seleccione una opcion"))
    match op:
        case 1:
            nombre=input("Ingrese el nombre del producto: ")
            precio=int(input("Ingrese el precio del producto: "))
            nuevo_producto={"nombre":nombre, "precio":precio}
            productos.append(nuevo_producto)
        case 2:
            print(productos)
        case 3:
            print("")
        case 4:
            print("Saliendo")
            break
        case _:
            print("Opcion invalida")



