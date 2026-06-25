
def suma(a, b):
    print(a+b)

suma(22, 3)

# notas1=[6.3,6.8, 3.7, 2.1]
# notas2=[6.3,1.8, 3.9, 2.1]

# def creaProm(n):
#    return round(sum(n)/len(n),1)


# print("El promedio del notas 1 es", creaProm(notas1))
# print("El promedio del notas 2 es", creaProm(notas2))

pinturas1=[
    {"color": "verde", "capacidad": 500, "formato": "tarro"}, #0
    {"color": "azul", "capacidad": 1500, "formato": "tarro"}, #1
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja"}, #2
    {"color": "purpura", "capacidad": 8500, "formato": "bolsa"}, #3
]
pinturas2=[
    {"color": "negro", "capacidad": 200, "formato": "tarro"}, #0
    {"color": "azul", "capacidad": 3500, "formato": "tarro"}, #1
    {"color": "naranja", "capacidad": 3500, "formato": "tinaja"}, #2
    {"color": "celeste", "capacidad": 7500, "formato": "bolsa"}, #3
]
listaColores=[]
listaCapacidad=[]
for i in pinturas1:
    # print(f"{i["color"]}")
    listaCapacidad.append(i["capacidad"])

print(min(listaCapacidad))


def mayorCap(lista):
    listaCapacidad=[]
    for p in lista:
        listaCapacidad.append(p["capacidad"])
    return max(listaCapacidad)

print(mayorCap(pinturas2))

# creree una funcion para buscar un color especifico
# pase la lista como argumento, y el color
# como segundo argumento. Retorne "Disponible"
# si el color existe. "NO existe" en caso contrario

def buscaColor(lista, color):
    for paint in lista:
        if color.lower()==paint["color"]:
            return "Disponibles"
    return "No existe"
busca=input("Ingrese el color a buscar: ")
print(buscaColor(pinturas1, busca))


nums=[20, 3, 7 ,11 , 67, 64, -8]

def buscaNumeros(lista, num):
    for n in lista:
        if n==num:
            return "Numero encontrado"
    return "No se encntro el numero ", num

numeroBuscar=int(input("Ingrese el numero a buscar: "))       
print(buscaNumeros(nums, numeroBuscar))

