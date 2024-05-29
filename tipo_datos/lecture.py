#crear una lista con 3 diccionarios de mascotas
mascotas=[
    {"nombre": "luna", "edad":3, "sexo": "hembra", "raza": "labrador"}, {"nombre": "max", "edad": 5, "sexo": "macho", "raza": "golden retriever"}, {"nombre": "bella", "edad": 2, "sexo": "hembra", "raza": "bulldog"}]
# mostrar la lista original
print("lista original:")
print(mascotas)
#editar el tercer registro cambiando la edad
mascotas[2]["edad"] = 4
# mostrar la lista con el tercer registro modificado
print("/nlista con el tercer registro modificado: ")
print(mascotas)