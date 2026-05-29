# crea un alista de frutas y realizar todos estas operaciones
    #   print("1.- Agregar Fruta")
    #   print("2.- Eliminar Fruta")
    #   print("3.- Actualizar Fruta")
    #   print("4.- Mostrar Frutas")





frutas=["Maracuyá", "Pera"]

def muestraFruta():
    print("-"*20)
    c=1
    for f in frutas:
        print(f"{c}.- {f}")
        c+=1
    print("-"*20)
def agregaFruta():
    nombreF=input("Ingrese el nombre del Fruta: ")
    frutas.append(nombreF)
def eliminaFruta():
    muestraFruta()
    opc=int(input("Seleccione el numero de la fruta a eliminar: "))
    frutas.pop(opc-1)
def actualiazaFruta():
    muestraFruta()
    opci=int(input("Seleccione el numero de la fruta a eliminar: "))
    nuevaFruta=input("ingrese la nueva fruta: ")
    frutas[opci-1]=nuevaFruta

def feria():
    while True:
      print("1.- Agregar Fruta")
      print("2.- Eliminar Fruta")
      print("3.- Actualizar Fruta")
      print("4.- Mostrar Frutas")
      print("5.- Salir")
      op=int(input("Seleccione una opcion: "))
      match op:
         case 1:
            agregaFruta()
         case 2:
            eliminaFruta()
         case 3:
            actualiazaFruta()
         case 4:
            muestraFruta()
         case 5:
            print("Salir")
            break
         case _:
            print("Opcion invalida")   



