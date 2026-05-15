# Uso y ejemplo s de while
# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except:
#         print("Solo numeros enteros")


code=6767
while True:
    try:
        pasw=int(input("Ingrese su clave: "))
        if code==pasw:
            print("Ingreso correcto")
            break
        else:
            print("Clave Invalida")
    except ValueError as er:
        print("Solo numeros enteros")
        print(er)