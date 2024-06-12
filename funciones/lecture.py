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
