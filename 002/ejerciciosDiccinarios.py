pokemons={
    1:{"nombre":"Ekans", "nivel": 19 },
    2:{"nombre":"Gastly", "nivel": 18 },
    3:{"nombre":"Eevee", "nivel": 12 }
} 
def mostrar():
    for p, z in pokemons.items():
        print(f"{p}.- {z} ")
    print("-"*30)
def eliminar():
    mostrar()
    # borrar_pokemon=input("Cual es el pokemon que va a liberar ?: ")
    # pokemons.remove(borrar_pokemon)
    borrar_pokemon=int(input("Cual es el pokemon que va a liberar ?: "))
    del pokemons[borrar_pokemon]
def actualizar():
    mostrar()
    actualizar=int(input("que pokemon desea actualizar: "))
    nombre=input("Ingrese el nombre del pokémon: ")
    nivel=input("Ingrese el nivel del pokémon: ")
    pokemons[actualizar]={"nombre":nombre, "nivel": nivel }
    print("actualizado con exito")
def agregar():
    pkm=input("Ingrese el nombre del pokemon: ")
    nvl=input("Ingrese el nivel del pokemon: ")
    pokemons[list(pokemons.keys())[-1]+1]={"nombre":pkm, "nivel": nvl }
def menuPokemon():
    while True:
        try:
            print("1.- Agregar Pokemon")
            print("2.- Eliminar Pokemon")
            print("3.- Actualizar Pokemon")
            print("4.- Mostrar Pokemons")
            print("5.- Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregar()
                case 2:
                    eliminar()
                case 3:
                    actualizar()
                case 4:
                    mostrar()
                case 5:
                    print("Saliendo")
                    break
                case _:
                    print("Opcion Invalida")

        except ValueError as e:
            print("Solo numeros enteros. Error",e)

# menuPokemon()

# print(list(pokemons.keys())[-1]+1)

pokemons={
    1:{"nombre":"Uva", "precio": 2000 },
    2:{"nombre":"Palta", "precio": 4000 },
    3:{"nombre":"Pera", "precio": 1500 }
} 


'''
            print("1.- Agregar Producto")
            print("2.- Eliminar Producto")
            print("3.- Actualizar Producto")
            print("4.- Mostrar Productos")
            print("5.- Comprar Productos")
            print("6.- Crear Boleta (calcula IVA) y Salir")
            op=int(input("Seleccione una opcion: "))'''