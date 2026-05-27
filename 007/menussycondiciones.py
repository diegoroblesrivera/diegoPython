## ejemplo de try

# try:
#     edad=int(input("Ingrese su edad: "))
# except ValueError as e:
#     print("Solo numeros enteros")
#     print("Error: ", e)
# else:
#     print("Bien hecho Woddy")

# camiones segun capacidad de carga
# 1-3 toneladas : camion chico
# 4-8 toneladas : camion mediano
# +9 toneladas : camion grande
# Solo se debe igresar valores enteros positivos
# La marca de camion debe tener no mas de 8 caracteres
# pero no menos de 3 
def menuCamiones():
    op=0
    chico=0
    mediano=0
    grande=0
    cap=0
    while  op!=6:
        try: 
            print("Seleccione una opcion")
            print("1.- Ingresar camion")
            print("2.- Mostrar totales")
            print("3.- Mostrar cantidad de camiones ")
            print("4.- Mostrar capacidad total de camiones")
            print("5.- Ingrese una marca de camion")
            print("6.- Salir ")
            op=int(input())
            match op:
                case 1:
                    while True:
                        try:
                            camion=int(input("Ingrese la capacidad de carga: "))
                            if camion>0:
                                cap+=camion
                                if 1<=camion<=3:
                                    chico+=1
                                elif 4<=camion<=8:
                                    mediano+=1
                                else:
                                    grande+=1
                                break
                            else:
                                print("EL valor debe ser positivo")
                        except ValueError as e:
                            print("Solo numeros enteros")
                            print("Error: ", e)
                        


                case 2:
                    print(f"EL total de camiones chicos es {chico}")
                    print(f"EL total de camiones medianos es {mediano}")
                    print(f"EL total de camiones grandes es {grande}")
                case 3:
                    print(f"EL total de camiones es {chico+mediano+grande}")
                case 4:
                    print(f"EL total de capacidad es {cap}")
                case 5:
                    marca=input("Ingrese la marca del camion: ")
                    if 3<=len(marca)<=8:
                        print(f"La marca {marca} fue ingresada correctamente")
                    else:
                        print(f"La marca {marca} no cumple los parametros")
                case 6:
                    print("Saliendo")
                case _:
                    print("Opcion Invalida")

        except ValueError as e:
            print("Solo numeros enteros")
            print("Error: ", e)

# Una Galeria de arte tiene 100 espacios para cuadros
# Preguntar cuantas persona vinieros a ver cuadros
# Al salir de la galeria , preguntar a cada personsa, cuantos cuadros vio
# POr cada persona . clasificar los cuadros vistos y no vistos
# 

galeria=100
vistos=0
noVistos=0
while True:
    try:    
        personas=int(input("Cuantas personas vinieron?: "))
        break
    except ValueError as e:
        print("Solo numeros enteros")
        print("Error: ", e)
for i in range(personas):
    while True:
        try:    
            cant=int(input("Cunatos cuadros vió?: "))
            vistos+=cant
            noVistos+=galeria-cant
            break
        except ValueError as e:
            print("Solo numeros enteros")
            print("Error: ", e)

print(f"El total de cuadros vistos fue {vistos}")
print(f"El total de cuadros NO vistos fue {noVistos}")

