# ejemplo y uso de try except




# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except ValueError as er:
#         print("Solo numeros enteros")
#         print(er)
        
# '''sacar promedio'''
    
# print("Ingrese 3 notas")
# total=0
# for i in range (3):
#     while True:
#         try:
#             n=float(input(f"Ingrese la nota {i+1}: "))
#             break
#         except:
#             print("Se debe ingresar numeros decimales")
#     total+=n
# prom=total/3
# print(f"El promedio es {prom}")


op=0
total=0
while op!=4:
    try:
        print("1.- PC $500.000")
        print("2.- LGTV 55 pulgadas $450.000")
        print("3.- Microondas Mademsa $100.000")
        print("4.- Salir")
        print("Seleccione una opcion")

        op=int(input())
        match op:
            case 1:
                print("El total a pagar es ",500000*1.19 )
                total+=500000*1.19
            case 2:
                print("El total a pagar es ",450000*1.19 )
                total+=450000*1.19
            case 3:
                print("El total a pagar es ",100000*1.19 )
                total+=100000*1.19
            case 4:
                print("Saliendo")
                print("El total a pagar es", total)
            case _:
                print("Opción inválida")
    except ValueError as e:
        print("SOlo numeros enteros. Error: ", e)





