#Uso y explicacion de diccionarios

alumno={
    "nombre": "Agusto Pino",
    "edad": 64,
    "nacionalidad": "chilena"
}


print(alumno)
print(alumno["nombre"])

alumno["Email"]="pino@gmail.com"
alumno["nacionalidad"]="peruana"
del alumno["edad"]
print(alumno)


# Crear un crud con diccionarios

def vegetalesMenu():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetal")
         print("5.- Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarVegetales()
               case 2:
                  eliminarVegetal()
               case 3:
                  actualizarVegetal()
               case 4:
                  mostrarVegetales()
               case 5:
                  print("Salir")
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:
         print("Error:",e)





