# return devuelve valores que podre hacer uso
#crear una funcion que retorne el numero 10 y muestra por terminal si es par
# siempre que el valor retorne mi funcion se utilize en mas sentencias u operaciones hacer uso de return
def diez():
    return 10
if diez()%2==0:
    print(" es par")
else:
    print("es impar")
#print solo muestra por terminal

#return cuando queremos que nuestra funcion devuelva o retorne un tipo de dato o un tipo de dato estrucuturado

#crear una funcion que me muestre el producto de dos numeros

def producto(a,b):
    return a*b

# crear una funcion que me retorne una lista de tres numeros
def lista_nunmeros():
    return [3,2,6]

# crear una funcion que por parametro reciba un nombre y retorne un mensaje de bievenida con el nombre
def mensaje(nombre):
    print(f"hola, {nombre}, bienvenido al chongo")
mensaje("jose")

# crear una funcion que reciba por parametro una lista de numeros y me devuelva el numero, mostrar por terminal el valor retornado por la funcion.
lista=(4,5,8,7,3,1)
def min(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
        return minimo
print(min(lista))

#crear una funcion que reciba como parametro el nombre y la edad de una persona mi funcion debera retornar un diccionario con los datos, luego mostrar por terminal el valor de retorno de mi funcion.
nombre=input("ingrese su nombre delincuente")
edad=int(input("ingrese su edad"))
def persona(nom,edad):
    # return {
    #       "nombre":nom,
    #       "edad":edad
    #  }
    return dict(
        nombre=nom
        edad=edad
    )
print(persona(nombre,edad))

Def suma(*args):
    nueva_lista=list(args)
    nueva_lista=
    print(args)
suma (4,7,8,5,2,4)
#empaquetado y desemppaquetado de argumentos nominales 
def alumnos(**kwargs):
    kwargs["nombre"]="abel"
    print(kwargs)
alumnos(nombre="miguel",apellido="largo",edad=30)

## EJEMPLOS DE LAMBDA
saludo=lambda:"hola, {n} , {a}"
print(saludo("ruth","castillo"))

#crear un programa anonimo que reciba ccomo parametro una lista de 5 numeros y retorne dos listas una con los numeros pares y otra con numeros impares

lista=[4,7,5,3,47,2,10,8,10]
pares=lambda 1:[n for n in lista if n%2==0]
impares=lambda 1:[n for n in lista if n%2!==0]
print(pares(lista))
print(impares(lista))
tarea
    
int(input())
    def mensaje(m):
        print(m)
    def pedir:nombre():
        nombre=input("ingresa su nombre")
        return nombre
    mensaje(pedir_nombre())
# map
lista=[4,7,8,5,2]
map(lambda x:x+1,lista) # por defecto retorna una lista


# tengo una lista de alumnos que todos ellos aprobaron y pasan al tecer semestre.
# tengo una lista toos estan con el segundo semestre por lo que tendremos qye crear una solucion que cambie el campi
# crear un programa que cambie el campo de semestre de 2 a 3
lista_alumnos=[ 
    {
        "nombre":"abel"
        "edad":36,
        "semestre":2
    },
    {
        "nombre":"anthony",
        "edad":40
        "semestre":2
    },
    {
        "nombre":"edith",
        "edad":50,
        "semestre":2
    }
]

alimnos_actualizados=list(map(lambda el:el["semestre"]+1,lista_alumnos))
print(alumnos_actualizado)[1]

# filter