#uso y  explicacion de match

# print("1.- Opcion 1")
# print("2.- Opcion 2")
# print("3.- Opcion 3")
# op=int(input("Seleccione una opcion: "))
# match op:
#     case 1:
#         print("Seleccionó la opcion 1")
#     case 2:
#         print("Seleccionó la opcion 2")
#     case 3:
#         print("Seleccionó la opcion 3")
#     case _:
#         print("Opcion Invalida")
# op=0
# total=0
# while op!=4:
#     print("1.- Xbox Series S $250.000")
#     print("2.- Sony PS5 $ $500.000")
#     print("3.- LGTV 60 Pulgadas $600.000")
#     print("4.- Salir")
#     op=int(input("Seleccione una opcion: "))
#     match op:
#         case 1:
#             print("El valor a pagar ", 250000*1.19)
#             total+=250000*1.19
#         case 2:
#             print("El valor a pagar ", 500000*1.19)
#             total+=500000*1.19
#         case 3:
#             print("El valor a pagar ", 600000*1.19)
#             total+=600000*1.19
#         case 4:
#             print("Saliendo")
#             print(f"El total a pagar es {total}")
#         case _:
#             print("Opcion Invalida")

# calculadora
# + - * /

def suma():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    print(f"El resultado es {num1+num2}")   
def resta():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    print(f"El resultado es {num1-num2}") 
def multi():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    print(f"El resultado es {num1*num2}")
def divi():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    print(f"El resultado es {num1/num2}")

def calculadora():
    op=0
    while op!=5:
        print("Que operacion desea realizar?")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicacion")
        print("4.- Division")
        print("5.- Salir")
        op=int(input("Selecione una opcion: "))
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
                print ("Saliendo")
            case _:
                print ("Opcion invalida")

calculadora()

#  Buscar 3 programs hechos en python 
# y crearlos como funciones
# llamarlos desde un menú


