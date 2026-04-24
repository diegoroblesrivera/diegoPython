# uso y explicacion de while
# cont=1
# while cont<=3:
#     print("Repeticion numero ", cont)
#     cont+=1


#ingrese PIN
pin=3232
baka=int(input("Ingrese su pin: "))
while pin!=baka:
    print("Pin incorrecto, intenta de nuevo")
    baka=int(input("Ingrese su pin: "))
print("Pin correcto")


