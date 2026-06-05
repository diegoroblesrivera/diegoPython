# uso y eplicacion de diccionarios

# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"piloto"
# }

# print(alumno)
# print(alumno["carrera"])

# for key ,value in alumno.items():
#     print(f"{key}= {value} ")
# print("---Cambios de datos---")
# # for dato ,valor in alumno.items():
# #     print(dato, valor )
# alumno["email"]="shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key ,value in alumno.items():
#     print(f"{key}= {value} ")

productos={
    1:{"nombre": "Control Inalambrico",
       "categoria": "Electronica",
       "precio": 45000},
    2:{"nombre": "Pilas Recargables",
       "categoria": "Insumos",
       "precio": 5000},
    3:{"nombre": "Pasta Termica",
       "categoria": "Computacion",
       "precio": 7000},
}

print(productos[1]["nombre"])

'''
Crear un diccionario de trabajadores 
'''

