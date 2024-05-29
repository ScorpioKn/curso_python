#crear una tisto de 5 alumnas atanacenaresos su nombre opettido y edad 
lista_alumnos [{ 
    "nombre":"abel",
    "apellido": "rojas", 
    "edad":27 
    },{
    "nombre":"cielo",
    "apellido": "castro", 
    "edad":23 
    },{
    "nombre": "ruth", 
    "apellido":"castillo", 
    "edad":18 
    },{
    "nombre":"flor", 
    "apellido":"lucana", 
    "edad":18 
     },{
    "nombre":"rocio", 
    "apellido":"lobo", 
    "edad":25 
    ]}
    #insertor al final de la Lista los datos de antoni 
    lista_alumnos.append({ 
        "nombre": "antoni",
        "apellido":"cuevas", 
        "edad":25 print(lista_alumnos) 
#eliminar de la Lista si existe Los datos de obel 
lista_alumnos.remove({ 
    "nombre": "abel", 
    "apellido": "rojas", 
    "edad":27 
    }) 
    print(lista_alumnos) 
    #atuano en la posicion a de Lo indice lista alumnos.
    index({ 
        "nombre": "rocio", 
        "apellido": "lobo", 
        "edad":25 
    }) 
print(lista_alumnos[indice])



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