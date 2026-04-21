'''Pedir a la clave al usuario y verificar 
que sea SHAZAM independiente de su case
( indiferente de mayusculas o minusculas)'''
# clave="SHAZAM"

# code=input("Ingrese su CLAVE: ")

# if code.upper()==clave:
#     print("Bienvenido al sistema")
# else:
#     print("Clave invalida")


'''Crear un nombre de usuario y verificar su que 
su largo esté entre 4 y 10 caracteres'''
# name=input("Crea un nombre de usuario: ")

# if 4< len(name) <10:
#     print("Usuario creado")
# else:
#     print("Nombre de Usuario invalido")


'''Cear un pin y que este tenga exactamente
4 digitos'''

pin=int(input("Ingrese un pin de 4 digitos"))

if pin>1000 and pin <9999:
    print("Pin creado")
else:
    print("Pin invalido")

if len(str(pin))==4:
    print("Pin creado")
else:
    print("Pin invalido")  