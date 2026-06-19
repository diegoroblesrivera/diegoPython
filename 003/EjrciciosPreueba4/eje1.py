## Crear un gestor de pacientes

pacientes=[
    {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
     "temperatura":39.6, "grave": True}, # 0
    {"nombre": " dON rAMON Baeza", "prevision": "Fodesa", 
     "temperatura":34.6, "grave": False},# 1
    {"nombre": " Señor Barriga ", "prevision": "Fonasa", 
     "temperatura":35.6, "grave": False}# 2
]

def mostrarPacientes():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        c=1
        for p in pacientes:
            print(f"{c} .-{p}")
            c+=1
        print("-"*50)
def quitarPaciente():
    mostrarPacientes()
    eli=int(input("Que paciente desea eliminar: "))
    pacientes.pop(eli-1)
def validarEstado(t):
    if t>39:
        return True
    else:
        return False
def ingresarPaciente():
    nombre=input("ingrese el nombre del paciente: ")
    prevision=input("ingrese la prevision del paciente: ")
    temp=float(input("ingrese la temperatura del paciente: "))
    pacientes.append({"nombre": nombre, "prevision": prevision, 
    "temperatura":temp, "grave": validarEstado(temp)})
def tomarTemperatura():
    mostrarPacientes()
    select=int(input("Que paciente le tomará la temperatura?: "))
    reg=float(input("Ingrese la temperatura: "))
    pacientes[select-1]["temperatura"]=reg
    pacientes[select-1]["grave"]=validarEstado(reg)
def cobrarAtencion():
    total=0
    mostrarPacientes()
    eli=int(input("Que paciente va  apagar?: "))
    prev=pacientes[eli-1]["prevision"]
    if prev.lower()=="fonasa":
        total=25000*0.46
    elif prev.lower()=="isapre":
        total=25000*0.73
    elif prev.lower()=="fodesa":
        total=25000*0.875
    else:
        print("Prevision no valida")
    print("EL total a pagar es", total)

def menuPacientes():
    while True:
        try:
            print("1.- Ingresar paciente")
            print("2.- Quitar paciente")
            print("3.- Tomar Temperatura")
            print("4.- Cobra atencion")
            print("5.- Mostrar Pacientes")
            print("9.- Salir")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    ingresarPaciente()
                case 2:
                   quitarPaciente()
                case 3:
                    tomarTemperatura()
                case 4:
                    cobrarAtencion()
                case 5:
                    mostrarPacientes()
                case 9:
                    print("Saliendo")
                    break
                case _:
                    print("Opción inválida")
        except Exception as e:
            print("Error:" , e)


menuPacientes()


