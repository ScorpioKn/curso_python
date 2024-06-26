## crear una funcion que reciba por argumento n numeros y retorne la lista con los numeros pares

def numeros_pares(*args):
    pares = [num for num in args if num % 2 == 0]
    return pares

# ejemplo de uso
resultado= numeros_pares(1,2,3,4,5,6,7,8,9,10)
print(resultado)

return numeros_pares
print(numeros_pares(8,5,4,7,9,25,4,7,12))

# por comprension
    #return [n for n in args if n%2==0]
print(numeros_pares(8,5,4,7,9,25,4,7,12)) 

# crear tres funcione spara los siguientes casos 
# calcular el numero menor 
# calcular el numero mayor
# calcular la suma de todos los numeros
# se le pasara por argumento n numeros

def min(**args):
    menor=args[0]
    for n in args
        if n<menor:
            menor=n
    return menor
def max(*args):
     mayor=args[0]
    for n in args
        if n<mayor:
            mayor=n
    return mayor
def sum(*args):
     suma=args[0]
    for n in args
        if n<suma:
            suma=n
    return suma

Valores=[4,7,8,5,2,]
print(Min(valores))
print(Max(valores))
print(Sum(valores))

#crear una lista de alumnos con los siguientes campos
# nombre,apellido,edad,celular,email
# 1. actualizar los registros con un campo mas todos tendran el campo de programa de estudio de enfermeria
# 2.buscar el segundo registro y actualizar su edad a 50 años.

# Crear una lista de alumnos con los campos solicitados
alumnos = [
    {"nombre": "Juan", "apellido": "Perez", "edad": 25, "celular": "999888777", "email": "lucho@example.com"},
    {"nombre": "Maria", "apellido": "Gomez", "edad": 30, "celular": "666555444", "email": "pedro@example.com"}
]

# Actualizar todos los registros con el campo "programa de estudio" de enfermería
for alumno in alumnos:
    alumno["programa de estudio"] = "enfermería"

# Buscar el segundo registro y actualizar su edad a 50 años con filter
segundo_registro = list(filter(lambda x: x["apellido"] == "Garriazo", alumnos))[0]
segundo_registro["edad"] = 50

# Imprimir la lista de alumnos actualizada
for alumno in alumnos:
    print(alumno)