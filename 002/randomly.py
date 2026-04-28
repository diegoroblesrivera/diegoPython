#uso y ejemplos de random

import random 
import time
# num=random.randint(1,10)
# print(num)

# for i in range(num):
#     print("hola deny")

# dado1=random.randint(1,6)
# dado2=random.randint(1,6)

# print(f"El dado 1 dio {dado1}")
# print(f"El dado 2 dio {dado2}")
# time.sleep(2)
# if dado1==dado2:
#     print("Se va  a la carcel")
# else:
#     print("Avance por favor")

# Adivina el numero

# crea un numero random entre 1 y 100
# Pide al usuario que adivine el numero
# si el usuario pone un numero mayor al generado
# debe decir " Te pasaste", en caso contrario
# " EL numero a adividar es mayor"
# Solo hay 5 posibilidades de adivinar.

# #forma 1
# numrandom=random.randint(1,100)

# for i in range (5):

#  adivinar=int(input("Adivine el numero: "))
#  print(numrandom)
#  if adivinar>numrandom:
#   print ("Menos")
#  else:
#   print("Más")
#  if adivinar==numrandom:
#   print (f"Usted a adivinado el numero era {numrandom}")
#   break
# else:

#   print (f"Usted no a adivinado el numero era {numrandom}")

# #forma 2
# print (" intente adivinar el numero")

# num=random.randint(1,100)
# intentos=5
# while intentos > 0:
#   adivina=int (input("ingrese un numero de 1 a 100:"))
#   #print(num)
#   if adivina > num:
#     print (" te pasaste, intentos restantes:", intentos-1)
#   elif adivina < num:
#     print (" el numero a adivinar es mayor , intentos restantes:", intentos-1)
#   else:
#     print ("felicidades, has adivinado el numero !!, tus intentos restantes son:", intentos)
#     break
#   intentos-=1
# if intentos == 0:
#   print (" lo siento, has agotado tus intentos, el numero era:", num)

# #forma 3

# rng = random.randint(1,100)
# guessed = False
# print("Bienvenido al juego de adivinar el numero. Tienes 5 intentos para adivinar un numero del 1 al 100.")
# for i in range(5):
#   num=int(input("Adivina el numero del 1 al 100: "))
#   if rng==num:
#     print("Felicidades adivinaste el numero")
#     guessed = True
#     break
#   else:
#     if rng<num:
#       print("El numero es menor")
#     else:
#       if rng>num:
#         print("El numero es mayor")
# if not guessed:
#   print("Lo siento, no adivinaste el numero. El numero era:", rng)


#KILLER INSTINC

# Dos peleadores se piden al inicio de la pelea
# Cada peleador inicia con 100 de HP 
# se debe hace una pelea por turnos 
# y cada golpe varia entre 7 y 18
# se termina el match cuando uno de los 2
# tiene su HP menor o igual a 0
# se debe mostrar el ganador al final
# BONUS: mostrar al barras de energia de cada peleador.
# time.sleep(2)
# Ludo 
# 1 jugador juega, y lanzar dos dados
# por cada unidad en el dado avanza una posicion en el tablero
# cuando llegue a 30 , gana
# mostrar cuantos turnos le tom
# llegar a la meta



# 3 personas juegan golf
# cada persona tiene la posibilidad de golpear
# y la distancia varia ente 60 y 190 metros
# mostrar al final, el golpe mas fuerte

j1=random.randint(60,190)
j2=random.randint(60,190)
j3=random.randint(60,190)
print(f"El jugador 1 lanzo la pelota {j1} metros ")
print(f"El jugador 2 lanzo la pelota {j2} metros ")
print(f"El jugador 3 lanzo la pelota {j3} metros ")
time.sleep(1)
if j1>j2 and j1>j3:
    print("El jugador uno, lanzó la pelota mas lejos")
elif j2>j3:
    print("El jugador dos, lanzó la pelota mas lejos")
elif j1==j2==j3:
    print("LOs tre mandaoron la peloda a la misma distancia")
else:
    print("El jugador tres, lanzó la pelota mas lejos")


