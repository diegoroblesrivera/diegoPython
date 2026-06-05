# EXPLICACION Y USO DE LISTAS
#      -5 -4  -3  -2   -1
lista=[8, 20, 12, 87, 1024]
#      0  1   2   3    4
import time      
# print(lista)
# print(lista[-4])

# for i in lista:
#     if i%2==0:
#         print(i, " es par") 
#     else:
#         print(i, " es impar") 
#     time.sleep(1)

# nombres=["Amaro", "Carlos", "Yony"]
# apellidos=["Vega", "Castillos", "Paredes"]

# print(nombres)
# # Amario Vega
# print(nombres[0], apellidos[0])

# for z in range(len(nombres)):
#     print(nombres[z], apellidos[z])




# Crear una lsita de 4 frutas
# mostrar lista por pantalla
# pedir al usuaro una fruta
#agregarla a la lista
# y volver a mostrar lista por pantalla

frutas=["Kiwi", "PERA", "Melon", "Uva"]

# for f in frutas:
#     print(f)

# fru=input("Agregue una fruta: ")
# frutas.append(fru)

# for f in frutas:
#     if f[-1].lower()=="a":
#         print(f, " termina con a")
#     else:
#         print(f, " NO termina con a")

# verificar si una fruta comienza con vocal

# vocales="aeiou"
# for f in frutas:
#     if f[0].lower() in vocales:
#         print(f"La fruta {f} comienza con vocal")
#     else:    
#         print(f"La fruta {f} NO comienza con vocal")

juguetes=["yo-yo", "tetris"]
def mostrar():
    h=1
    for j in juguetes:
            print(h ,j )
            h+=1
def eliminar():
    mostrar()
    o=int(input("Que JUGUETE desea eliminar: "))
    juguetes.pop(o-1)
def actualizar():
    mostrar()
    actualizar=int(input("Que juguete desea actualizar?: "))
    nuevo_nombre=input("Ingrese nuevo nombre: ")
    juguetes[actualizar-1]=nuevo_nombre
'''  print("-"*20)
print("1.- Agregar Juguete")
print("2.- Eliminar Juguete")
print("3.- Actualizar Juguete")
print("4.- Mostar Juguetes")
print("5.- Salir")'''
def menuJuguetes():
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
                        agregar=input("QUe juguete desa agregar?: ")
                        juguetes.append(agregar)
                    case 2:
                        eliminar()
                    case 3:
                        actualizar()
                    case 4:
                        mostrar()
                    case 5:
                        print("Saliendo")
                        break
                    case _:
                        print("Opcion invalida")

        except Exception as e:
            print( " error: " , e)


