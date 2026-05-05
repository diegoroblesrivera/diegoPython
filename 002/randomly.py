#uso y ejemplos de random

import random , time
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
# cuando llegue a 50 , gana
# mostrar cuantos turnos le tom
# llegar a la meta



# # 3 personas juegan golf
# # cada persona tiene la posibilidad de golpear
# # y la distancia varia ente 60 y 190 metros
# # mostrar al final, el golpe mas fuerte

# j1=random.randint(60,190)
# j2=random.randint(60,190)
# j3=random.randint(60,190)
# print(f"El jugador 1 lanzo la pelota {j1} metros ")
# print(f"El jugador 2 lanzo la pelota {j2} metros ")
# print(f"El jugador 3 lanzo la pelota {j3} metros ")
# time.sleep(1)
# if j1>j2 and j1>j3:
#     print("El jugador uno, lanzó la pelota mas lejos")
# elif j2>j3:
#     print("El jugador dos, lanzó la pelota mas lejos")
# elif j1==j2==j3:
#     print("LOs tre mandaoron la peloda a la misma distancia")
# else:
#     print("El jugador tres, lanzó la pelota mas lejos")




# # Loteria

# # generar 3 numeros entre 1 y 9
# # luego, tirar numeros al azar en ese rango 
# # Cuando todos los numeros coincidan con los primeros 3 
# # generados, debe poner "ganaste"
# # contar , cuantos numeros tuvo que tirar
# # para ganar la loteria .
# n1=random.randint(1,9)
# n3=random.randint(1,9)
# n2=random.randint(1,9)
# t1=False
# t2=False
# t3=False
# nums=0
# print(f"Los numeros generados son: {n1}, {n2} y {n3}")
# while not t1 or not t2 or not t3:
#     numerito=random.randint(1,9)
#     print("EL numero es", numerito)
#     time.sleep(1)
#     if numerito==n1:
#         t1=True
#     if numerito==n2:
#         t2=True
#     if numerito==n3:
#         t3=True
#     nums+=1
# print(f"GANASTE, en {nums} turnos")



'''
Fabrica de enlatados
Se necesita hacer el algoritomo de productos enlatados
Se debe consultar el peso del producto( en gramos) ( solo valores positivos)
El porcentaje de sodio en él ( solo valores entre 1 y 100)
y si se va a vender nacional o internacionalmente
Considerar los criterios en la siguiente tabla

menos de 500 grs, lata normal
501 hassta 1500 bgr, lata mediana
1501 y mas , lata grande
si el sodio es menos de 5%, lata queda igual
si es entre 5% y 8% lata especial
si tiene 9% o mas, lata acorazada
a las latas internacionales, se le debbe pegar 
in sticker de validacion sanitaria

Ej:800, 7%, 2==> lata mediana espacial con sticker sanitario
'''










# peso=int(input("Ingrese el peso del producto: "))
# while peso<1:
#     print("Ingrese solo valores positivos")
#     peso=int(input("Ingrese el peso del producto: "))
# sodio=int(input("Ingrese el porcentaje de sodio del producto: "))
# while sodio<1 or sodio>100:
#     print("El porcentaje solo debe ser entre 1 y 100")
#     sodio=int(input("Ingrese el porcentaje de sodio del producto: "))
# mercado=int(input("Ingrese el mercado del producto 1.- Nacional , 2 Internacional:"))

# while mercado<1 or mercado>2:
#     mercado=int(input("Ingrese el mercado del producto 1.- Nacional , 2 Internacional:"))


# # hola=input()
# # hola="Como andamios?"
# if peso<500:
#     lata="Lata normal"
# elif 500<peso<1501:
#     lata="Lata mediana"
# elif peso>1500:
#     lata="Lata grande"

# if sodio<5:
#     sod=""
# elif 5<sodio<=8:
#     sod="especial" 
# elif sodio>8:
#     sod="acorazada"

# if mercado==1:
#     sticker=""
# else:
#     sticker="con sticker sanitario"

# print(f"{lata} {sod} {sticker}") 



'''
Realizar las clasificacion de peces
Generar una candidad aleatorea de captura de peces
entre 10 y 20
Capturar peces y clasificarlos por su peso
para saber como se venderan
800 grs o menos, a lata
801 o mas, a la placha
Contar cuando quedaron a la pancha y 
cuantos quedatos para embasar en lata
'''

peces=random.randint(10,20)
p_lata=0
p_plancha=0
print(f"Campturamos {peces} peces")
for p in range(peces):
    pesoP=random.randint(100, 2000)
    print(f"EL peso del pez {p} es de {pesoP}")
    if pesoP<800:
        p_lata+=1
    else:
        p_plancha+=1
print(f"La cantidad de leces para enlatar es {p_lata}")
print(f"La cantidad de leces para la plancha es {p_plancha}")





