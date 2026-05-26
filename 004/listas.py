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


# ## DICCIONARIO

# alumno={
#     "nombre":  "Wanda MAximoff",
#     "carrera": "Informatica",
#     "edad":    24
# }

# # # recorrer cada elemento de un diccionario
# # print(alumno)
# for key, value in alumno.items():
#     print(key, value)
# #buscar
# print(alumno["edad"])

# # insersion 
# alumno["email"]="wanda@gamail.com"

# # actualizacion
# alumno["edad"]=26

# # Eliminacion
# del alumno["carrera"]


# for key, value in alumno.items():
#     print(key, value)

## Cree un diccionario de 3 productos, cada uno 
# con nombre, categoria, precio.

productos={
    1:{"nombre": "Laptop",
       "categoria": "Electronica",
       "precio": 400000},
    2:{"nombre": "Chaqueta",
       "categoria": "Vestuario",
       "precio": 40000},
    3:{"nombre": "Caable HDMI",
       "categoria": "Accesorios",
       "precio": 5000},

}

print(productos[3]["categoria"])
