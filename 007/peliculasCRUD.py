peliculas={
   1:{"nombre": "Inception", "anio": 2010, "director": "Nolan"},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}

## Crear n dioconario de lo que usted prefiera
# que ten al menos 3 propiedades


##Diccionario con diccionarios
productosDicc={
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}
carrito=[]
productosDicc[4]={"nombre": "Piña", "precio": 3500}
def agregarProducto():
   print("Cual es el nombre del producto?")
   nombre = input()
   print("cual es el precio?")
   precio = int(input())
   nuevoKey=list(productosDicc.keys())
   nuevoKey.sort()
   productosDicc[nuevoKey[-1]+1]= {"nombre": nombre, "precio": precio}
def MostrarProducto():
   for key, producto in productosDicc.items():
      print(f"{key} .-{producto}")
def eliminarProducto():
   MostrarProducto()
   try:
      borrar=int(input("Cual Producto borrará?: "))
      if borrar in productosDicc.keys():
         del productosDicc[borrar]
      else:
         print("Producto no existe")
   except Exception as e:
      print("Error:", e)
def actualizarProducto():
   MostrarProducto()
   num=int(input("Que producto desea actualizar?: "))
   if num in productosDicc.keys():
      nombre=input("Cual es el nombre nuevo?: ")
      precio=int(input("Cual es el precio nuevo?: "))
      productosDicc[num]={"nombre": nombre, "precio": precio}
   else:
      print("Producto no existe")

def comprar():
   while True:
      MostrarProducto()
      try:
         com=int(input("Que producto va a comprar?(0 para salir): "))
         if com==0:
            break
         if com in productosDicc.keys():
            carrito.append(productosDicc[com])
      except Exception as e:
         print("Error:", e)

def crearBoleta():
   total=0
   print("-"*30, "0", "-"*30)
   print("Bienvenido a minimarket Bender")
   for prod in carrito:
      print(f"{prod["nombre"]}___${prod["precio"]}")
      total+=prod["precio"]
   print("-"*30, "0", "-"*30)
   print(f"El total neto es{total} y el IVA es{total*0.19}")
   print(f"El total a pagar es{round(total*1.19)} ")
   print("Gracias por venir a minimarket Bender")
   print("-"*30, "0", "-"*30)
# print(productosDicc[2]["precio"])  # precio de la pera
# print(productosDicc[3]["nombre"])  # nombre de la cebolla

# for num, veg in productosDicc.items():
#     print(f"{num}.- {veg}")

##Lista con diccionarios
productosList=[
   {"nombre": "Maracuyá", "precio": 3000}, #0
   {"nombre": "Pera", "precio": 1500},     #1  
   {"nombre": "Cebolla", "precio": 1200}   #2
]

# print(productosList[2]["precio"]) #precio de la cebolla
# print(productosList[0]["nombre"]) #nombre de la naracuya



def vegetalesMenuDiccionario():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetal")
         print("5.- Comprar")
         print("6.- Crear Boleta y Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarProducto()
               case 2:
                  eliminarProducto()
               case 3:
                  actualizarProducto()
               case 4:
                  MostrarProducto()
               case 5:
                  print("Comprar")
                  comprar()
                  print(carrito)
               case 6:
                  crearBoleta()
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:
         print("Error:",e)
vegetalesMenuDiccionario()