## uso y explicacion de ramdom

import random
import time


# num=random.randint(1,10)
# print(num)


# num=random.randint(1,10)

# for i in range(num):
#     print("Hola Checha")


# strike=random.randint(10, 70)

# if strike>50:
#     print("Its a critical hit. Damage ", strike)
# else:
#     print("Its not very effective. Damage", strike)

# 3 personas juegan golf
# cada persona tiene la posibilidad de golpear
# y la distancia varia ente 60 y 190
# mostrar al final, el golpe mas fuerte


# j1=random.randint(60,190)
# j2=random.randint(60,190)
# j3=random.randint(60,190)

# print(f"El jugador 1 golpeo la pelota a {j1} metros")
# print(f"El jugador 2 golpeo la pelota a {j2} metros")
# print(f"El jugador 3 golpeo la pelota a {j3} metros")
# time.sleep(2)
# if j1>j2 and j1>j3:
#     print("El jugador uno hizo el tiro mas lejano")
# elif j2>j3:
#     print("El jugador dos hizo el tiro mas lejano")
# else:
#     print("El jugador tres hizo el tiro mas lejano")


#KILLER INSTINC

# Dos peleadores se piden al inicio de la pelea
# Cada peleador inicia con 100 de HP 
# se debe hace una pelea por turnos 
# y cada golpe varia entre 7 y 18
# se termina el match cuando uno de los 2
# tiene su HP menor o igual a 0
# se debe mostrar el ganador al final
# BONUS: mostrar al barras de energia de cada peleador.

p1=input("Ingrese el nombre del peleador 1: ")
p2=input("Ingrese el nombre del peleador 2: ")
hp1=100
hp2=100
turno=random.randint(1,2)

while hp1>0 and hp2>0:
    if turno%2==0:
        print(f"turno de {p1}")
        atk=random.randint(7,18)
        print(f"el {p1} ataca con {atk} ")
        hp2-=atk
        print(f"El hp de {p2} es {hp2}")
        time.sleep(1)
    else:
        print(f"turno de {p2}")
        atk=random.randint(7,18)
        print(f"el {p2} ataca con {atk} ")
        hp1-=atk
        print(f"El hp de {p1} es {hp1}")
        time.sleep(1)
    turno+=1
    print(p1, "█"*hp1)
    print(p2, "█"*hp2)
if hp1>hp2:
    print("EL ganador es ", p1)
else:
    print("EL ganador es ", p2)