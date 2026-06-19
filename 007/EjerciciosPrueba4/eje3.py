notas=[4.6, 7.0,3.4,6.6 , 3.9, 6.8]

# crear un a funcion para poder pasarle la lista
# como parametro y msotrar el promedio
# mostrar si aprueba o reprueba

def calculaProm(n):
    return round(sum(n)/len(n), 1)
print("El promedio es ", calculaProm(notas))

print(max(notas))
print(min(notas))

peliculas=[
    {"titulo": "Inception", "director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "anio": 2010 },
    {"titulo": "Jurassic Park", "director": "Steven Spilberg",
     "genero": "Ciencia Ficcion", "anio": 1993 },
    {"titulo": "Se7en", "director": "David Fincher",
     "genero": "Thiller", "anio": 1997 },

]


# crear un gestor de peliculas
# EL titulo debe tener mas de 2 caracteres
# el año debe ser mayor a 1960 y debe der menor al año actual
# El director debe tener nombre y apellido
# mostar el sigueinte menú
#  
'''
1.- ingresar Pelucula
2.- quitar Pelucula
3.- ingresar Pelucula
4.- Mostar Peluculas
5.- Mostrar solo los titulos
6.- Ordenar de mas reciente a mas antigua
7.- Salir
'''






