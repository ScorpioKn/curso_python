# 2. crear una lista con 3 diccionarios donde tendran los datos de sus mascotas (nombre, edad, sexo, raza)
dic=[
    {},
    {},
 ]

#tareas
# mostrar la lista con los 4 diccionarios
# editar el 3 registro y cambiarle la edad sin modificar la lista original
#mostrar la lista original y luego la lista con el 3 registro modificado

resolucion

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