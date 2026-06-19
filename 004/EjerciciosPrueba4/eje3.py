notas=[4.6, 2.2, 1.8, 6.8]

# crear un a funcion para poder pasarle la lista
# como parametro y msotrar el promedio
# mostrar si aprueba o reprueba



def promedio(notas):
    return round(sum(notas)/len(notas), 1)
if promedio(notas)<4:
     print("El alumno reprobó con",promedio(notas) )
else:
     print("El alumno aprobó con",promedio(notas) )


print(max(notas))
print(min(notas))

peliculas=[
    {"titulo": "Inception", "director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "anio": 2010, "rate": 8.9 },
    {"titulo": "Jurassic Park", "director": "Steven Spilberg",
     "genero": "Ciencia Ficcion", "anio": 1993 , "rate": 9.6},
    {"titulo": "Se7en", "director": "David Fincher",
     "genero": "Thiller", "anio": 1997 , "rate": 9.3},
]

for p in peliculas:
    print(p["titulo"])
# crear un gestor de peliculas
# EL titulo debe tener mas de 2 caracteres
# el año debe ser mayor a 1960 y debe der menor al año actual
# El director debe tener nombre y apellido
# mostar el sigueinte menú
'''1.- ingresar Pelicula
2.- quitar Pelicula
3.- Actualizar Pelicula
4.- Mostar Peliculas
5.- Mostrar solo los titulos
6.- Mostrar los años de las peliculas ordenados
7.- Mostrar meplicula mejor calificada
9.- Salir
'''










