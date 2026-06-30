#Funciones guia examen
 
 
 
autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}
 
 
 
def autos_vendidos_por_marca(marca):
    total = 0
    for id_auto, datos in autos.items():
        if datos[0].lower() == marca.lower():
            if operaciones[id_auto][1] != 'Pendiente':
                total += 1
    print(f'El número total de autos vendidos de la marca {marca.upper()} es {total}')
 
 
 
def busqueda_por_anio(anio_min, anio_max):
    elementos_encontrados = []
 
 
    for id_auto, datos in autos.items():
        marca = datos[0]
        modelo = datos[1]
        anio = datos[2]
 
 
        if anio_min <= anio <= anio_max:
            if operaciones[id_auto][1] == 'Pendiente':
                elementos_encontrados.append(f'{marca} {modelo} -- {id_auto}')
    
    if elementos_encontrados:
        elementos_encontrados.sort()
        print(elementos_encontrados)
    else:
        print('No se han encontrado elementos')
 
 
 
 
## MAIN
 
 
#test autos_vendidos_por_marca
#marca = input('Ingrese la marca a buscar: ')
#autos_vendidos_por_marca(marca)
 
 
#test busqueda_por_anio
 
 
while True:
    try: 
        anio_inicio = int(input('Ingrese en año de inicio de la búsqueda: '))
        anio_termino = int(input('Ingrese en año de término de la búsqueda: '))
        busqueda_por_anio(anio_inicio,anio_termino)
        break
    except:
        print('Los años ingresados deben ser número enteros')