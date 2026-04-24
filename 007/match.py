# explicacon u usa de match
# op=0
# total=0
# while op!=4:
#     print("1.- PC Ryzen $800.000")
#     print("2.- LGTV 55 Pulgadas $450.000 ")
#     print("3.- Parlante JBL Pure Sounf $90.000")
#     print("4.- Salir")
#     print("Seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             print("Tiene que pagar", 800000*1.19)
#             total+=800000*1.19
#         case 2:
#             print("Tiene que pagar", 450000*1.19)
#             total+=450000*1.19
#         case 3:
#             print("Tiene que pagar", 90000*1.19)
#             total+=90000*1.19
#         case 4:
#             print("Saliendo")
#             print(f"El total a pagar con IVA es {round(total,2)}")
#         case _:
#             print("Opción inválida")

def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado es {n1+n2}")
def resta():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado es {n1-n2}")
def multi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado es {n1*n2}")
def divi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado es {n1/n2}")

def calculadora():
    op=0
    while op!=5:
        print("1.- Sumar")
        print("2.- Restar")
        print("3.- Multiplicar")
        print("4.- Dividir")
        print("5.-  Salir")
        op=int(input("Seleccione una operación: "))
        match op:
            case 1:
                suma()
            case 2:
                resta()
            case 3:
                multi()
            case 4:
                divi()  
            case 5:
                print("Saliendo")
            case _:
                print("Opcion inváida")

# calculadora()

## seleccionar 3 programas que ya hemos hecho
# convertirlos en funcion
# ponerlos en un menu
# y llamarlos por su nombre

def nombreUsuario():
    nombre=input("Ingrese su nombre de usuario: ")

    if 4<=len(nombre)<=10 :
        print("Usuario correcto")
    else:
        print("Usuario fuera de rango")
def sumatoria():
    num=int(input("Ingrese un numero: "))
    suma=0
    for i in range(num):
        suma=suma+i+1
    print("El resultado de la suma es", suma )

def multiNotas():
    notas=int(input("Ingrese la cant de notas: "))
    suma=0
    for i in range(notas):
        n=float(input(f"Ingrese la nota {i+1}: "))
        suma=suma+n
    prom=suma/notas
    print("El promedio es",round(prom,1) )

    if prom>=4:
        print("Alumno aprobado")
    else:
        print("Alumno reprobado")

def variosProgramas():
    op=0
    while op!=4:
        print(''' Menu
        1.- Nmbre usuario
        2.- Sumatoria
        3.- Multinotas
        4.- Salir
        Seleccione una opcion''')
        op=int(input())
        match op:
            case 1:
                nombreUsuario()
            case 2:
                sumatoria()
            case 3:
                multiNotas()
            case 4:
                print("Saliendo")
            case _:
                print("Opcion inváida")


variosProgramas()




