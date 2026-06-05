
vegetales={
   1:"Maracuyá",
   2:"Pera",
   3:"Cebolla",
   7:"Papa"
}

# print(len(vegetales))

def agregaVegetal():
    nombreF=input("Ingrese el nombre del Vegetal: ")
    vegetales[list(vegetales.items())[-1][0]+1]=nombreF
def muestraVegetal():
    for key, value in vegetales.items():
        print(key, ".-" , value)
    print("-"*30)
def eliminaVegetal():
    muestraVegetal()
    borra=int(input("Cual desea eliminar?: "))
    del vegetales[borra]
def actualiazaVegetal():
    muestraVegetal()
    actualiza=int(input("Cual desea actualizar?: "))
    nuevo_vegetal=input("Cual es el nombre nuevo?: ")
    vegetales[actualiza]=nuevo_vegetal
def vegetalesMenu():
    while True:
        try:
            print("1.- Agregar Vegetal")
            print("2.- Eliminar Vegetal")
            print("3.- Actualizar Vegetal")
            print("4.- Mostrar Vegetal")
            print("5.- Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregaVegetal()
                case 2:
                    eliminaVegetal()
                case 3:
                    actualiazaVegetal()
                case 4:
                    muestraVegetal()
                case 5:
                    print("Salir")
                    break
                case _:
                    print("Opcion invalida")  
        except Exception as e:
            print("Error :", e)

# vegetalesMenu()


productosDicc={
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}


print(productosDicc[2]["precio"])  # precio de la pera
print(productosDicc[3]["nombre"])  # precio de la pera

productosList=[
   {"nombre": "Maracuyá", "precio": 3000},
   {"nombre": "Pera", "precio": 1500},
   {"nombre": "Cebolla", "precio": 1200}
]

print(productosList[2]["precio"]) #precio de la cebolla
print(productosList[0]["nombre"]) #precio de la cebolla
