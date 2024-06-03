# Crear una lista con 3 diccionarios de mascotas
mascotas = [
    {"nombre": "Luna", "edad": 3, "sexo": "Hembra", "raza": "Labrador"},
    {"nombre": "Max", "edad": 5, "sexo": "Macho", "raza": "Golden Retriever"},
    {"nombre": "Bella", "edad": 2, "sexo": "Hembra", "raza": "Bulldog"}
]

# Mostrar la lista original
print("Lista Original:")
print(mascotas)

# Editar el tercer registro cambiando la edad
mascotas[2]["edad"] = 4

# Mostrar la lista con el tercer registro modificado
print("\nLista con el Tercer Registro Modificado:")
print(mascotas)




# un empresario de alquiler de autos desea guardar en una base de datos la informacion de sus vehiculos, proceso que desea automatizar con un sistema informatico, las acciones que puede realizar el empresario son ver las listas de autos que tiene, podra tambien actualizar la lista y agregar un nuevo vehiculo

#####
# casos de uso

# programacion

# yo como empresario

# puedo observar la lista de autos que tengo

# puedo actualizar la lista de autos

# puedo agregar nuevos vehiculos

# puedo ingresar datos de los vehiculos

# Lista de autos
autos = [
    {"marca": "Toyota", "modelo": "Corolla", "año": 2020, "precio": 30000},
    {"marca": "Honda", "modelo": "Civic", "año": 2019, "precio": 28000},
    {"marca": "Ford", "modelo": "Mustang", "año": 2021, "precio": 45000}
]
def ver_lista_autos(lista_autos):
    print("Lista de Autos:")
    for idx, auto in enumerate(lista_autos, 1):
        print(f"Auto {idx}: Marca: {auto['marca']}, Modelo: {auto['modelo']}, Año: {auto['año']}, Precio: ${auto['precio']}")

def actualizar_auto_manual(lista_autos, indice):
    if indice >= 1 and indice <= len(lista_autos):
        print(f"Ingrese la nueva información para el Auto {indice}:")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = int(input("Año: "))
        precio = float(input("Precio: "))
        lista_autos[indice - 1] = {"marca": marca, "modelo": modelo, "año": año, "precio": precio}
        print("Información del auto actualizada correctamente.")
    else:
        print("Índice de auto no válido.")
def agregar_auto(lista_autos, nuevo_auto):
    lista_autos.append(nuevo_auto)
    print("Nuevo auto agregado correctamente.")
ver_lista_autos(autos)
actualizar_auto_manual(autos, 2)
nuevo_auto = {"marca": "Chevrolet", "modelo": "Camaro", "año": 2022, "precio": 50000}
agregar_auto(autos, nuevo_auto)
ver_lista_autos(autos)