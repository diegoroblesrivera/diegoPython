# ## DICCIONARIO

alumno={
    "nombre":  "Wanda MAximoff",
    "carrera": "Informatica",
    "edad":    24
}

##Hacer diccionario con el eelemento que usted quiera
# EJ: pelicuals , juego, pokemon, carts coleccionables, etc
# Debe tener al menos 4 propiedades
# Y debe hacer cambios de datos
# Insersion, borrado, actualizacion y muestra de los mismos.

# # recorrer cada elemento de un diccionario
# print(alumno)
# for key, value in alumno.items():
#     print(key, value)
# #buscar
# print(alumno["edad"])

# # insersion 
# valor=input("QU variable va a agregar?: ")
# tel=int(input("Ingrese el numero de telefono: "))
# alumno[valor]=tel
# alumno["email"]="wanda@gamail.com"

# # actualizacion
# edad=int(input("Digame su edad"))
# alumno["edad"]=edad

# # Eliminacion
# del alumno["carrera"]


# for key, value in alumno.items():
#     print(key, value)

## Cree un diccionario de 3 productos, cada uno 
# con nombre, categoria, precio.

# productos={
#     1:{"nombre": "Laptop",
#        "categoria": "Electronica",
#        "precio": 400000},

#     2:{"nombre": "Chaqueta",
#        "categoria": "Vestuario",
#        "precio": 40000},

#     3:{"nombre": "Caable HDMI",
#        "categoria": "Accesorios",
#        "precio": 5000},

# }

# #print(productos[3]["categoria"])
# print(productos)
# nom=input("Ingrese el nombre del productos: ")
# cat=input("Ingrese la categoria del productos: ")
# precio=int(input("Ingrese el precio del productos: "))

# productos[4]={"nombre": nom,
#        "categoria": cat,
#        "precio": precio}

# print(productos)

temperaturas={
    "lunes": 15,
    "martes": 18,
    "miercoles":14,
    "jueves":9,
    "viernes":19
}

# print(temperaturas)
maximos=[]
for dia, maxi in temperaturas.items():
   print(dia, maxi)
   maximos.append(maxi)
print(max(maximos))


alumno={
    "nombre":  "Wanda MAximoff",
    "carrera": "Informatica",
    "edad":    24
}
def mostrar():
    for key, value in alumno.items():
        print(key, value)
    print("-"*20)
def agregar():
    key=input("Que dato va a agregar?: ")
    value=input("ingrese el valor del dato: ")
    if value.isdigit():
        value=int(value)
    alumno[key]=value
def eliminardato():
    mostrar()
    elminar=input("cual dato desea eliminar: ")
    del alumno[elminar]
def actulizar():
    mostrar ()
    dato=input("Digame que actualizara: ")
    valor=input("cual sera el nuevo valor ")
    alumno[dato]=valor
print(alumno.items())
print(alumno.keys())
print(alumno.values())


while True:
    try:
        print("1.- Agregar dato")
        print("2.- Borrar datos")
        print("3.- Actualizar dato")
        print("4.- Mostrar datos")
        print("5.- Salir")
        op=int(input("Seleccione un opcion: "))
        match op:
            case 1:
                agregar()

            case 2:
                eliminardato()
            case 3:
               actulizar()
            case 4:
                mostrar()
            case 5:
                print("Saliendo")
                break
            case _:
                print("Opcion bo válida")
                
    except Exception as e:
        print("Error:", e)
