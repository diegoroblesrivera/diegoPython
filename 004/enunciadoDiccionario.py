## crear un gestor de estacionamiento
# Un estacionamiento tiene 4 pisos
# y cada piso tiene 20 espacios
#  Preguntar cuando entra un vehiculo, que tipo de vheiculo es
# vehículo ligero 2000
# vehículo mediano 3000
# vehículo pesado 3500

# luego , acomodarlo en algun lugar de algun piso disponible.
# el menu dsebe tener las sigueintes alternativas
''' 1.- ingresar vehiculo
2.- contar ganancias
3.- contar vehiculos'''

# usa lista o diccionario segun le acomode mas

parking={
    1:[2000, 3500, 2000,2000, 3500, 2000,2000, 3500, 2000],
    2:[],
    3:[],
    4:[]

}

print(len(parking[1]))

def parkingAutos():
    while True:
        try:
            print(''' 1.- ingresar vehiculo
                    2.- contar ganancias
                    3.- contar vehiculos
                    4.- Mostrar
                    5.- Salir''')
            op=int(input("Seleccione un a opcion: "))
            match op:
                case 1:
                    print("Ingresar vheiculo nuevo")
                    tipo=int(input("Que tipo es?: \n1.-Ligero\n2.-Mediano\n3.-Pesado"))
                    if tipo==1:
                        valor=2000
                    elif tipo==2:
                        valor=3000
                    elif tipo==3:
                        valor=3500
                    else:
                        print("Vehiculo invalido")
                    piso=int(input("EN que piso va?: "))
                    if piso in [1,2,3,4]:
                        if len(parking[piso])<10:
                            parking[piso].append(valor)
                            print("Agregado al piso", piso)
                        else:
                            print("Piso lleno")
                case 2:
                    totalGanancias=0
                    print("Contando Ganancias")
                    for piso in parking.values():
                        totalGanancias+=sum(piso)
                    print(f"El total recudado es {totalGanancias}")
                case 3:
                    totalAutos=0
                    for piso in parking.values():
                        totalAutos+=len(piso)
                    print("El total de autos en el parking es:", totalAutos)

                    
                case 4:
                    for h, t in parking.items():
                        print(h, ".- ", t)
                case 5:
                    print("Saliendo")
                    break
                case _:
                    print("Opción inválida")
        except Exception as e:
            print("Error:", e)

parkingAutos()
