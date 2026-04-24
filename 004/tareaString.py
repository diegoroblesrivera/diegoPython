# '''Pedir a la clave al usuario y verificar 
# que sea SHAZAM independiente de su case
# (sin inporta si son mayusculas o minusculas)'''
# # clave="SHAZAM"
# # code=input("Ingrese la clave: ")

# # if clave==code.upper():
# #     print("Acceso concedido")
# # else:
# #     print("Clave invalida")


# '''Crear un nombre de usuario y verificar su que 
# su largo esté entre 4 y 10 caracteres
# '''
# # user=input("Ingrese nombre de usuario:")

# # if len(user)<4 :
# #     print("deben ser al menos 4 caracteres")
# # elif len(user)>10:
# #     print("Error, el max es 10 caracteres")
# # else:    
# #     print("Usuario creado correctamente")
# '''Cear un pin y que este tenga exactamente
# 4 digitos'''

# pin=int(input("Ingrese su pin: "))

# if len(str(pin))==4:
#     print("Pin creado")
# else:
#     print("Pin erroneo")

# if 1000<pin <9999:
#     print("Pin creado")
# else:
#     print("Pin erroneo")



# # Definir 2 candidatos. Preguntar la cantidad de votantes
# # Preguntar a cada votante por quien votará mostrando 
# # las alternativas. Contar los votos y mostrar resultados.
# # Definir el ganador y considerar un empate.

toon1=input("Ingrese el Toon 1: ")
toon2=input("Ingrese el Toon 2: ")
v1=0
v2=0
num=int(input("Ingrese la acnt de votantes: "))

for i in range(num):
    voto=int(input(f"Por quein votará. 1.-{toon1} 2.- {toon2} "))
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print("Voto no valido")
if v1>v2:
    print(f"El ganador es {toon1} con {v1} votos")
elif v1<v2:
    print(f"El ganador es {toon2} con {v2} votos")
else:
    print("Fue empate")
