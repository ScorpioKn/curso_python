#primer ejemplo if estructurado
edad:int=int(input("escribe tu edad: "))
if edad>=18
    print ("eres mayor")
else:
    print ("eres menor de edad")

#segundo ejemplo if almacenado en variable
edad_dos:int=int(input("escribe tu edad: "))
respuesta:str="eres mayor" if edad_dos>18 else "eres menor"
print(respuesta)

#crear un programa que me imprima 5 vocales
vocales = ["a", "e", "i", "o", "u"] 
for vocal in vocales:
    print(vocal)
 vocales:str="aeiou"
 for n in range(o,5):
    print(vocales)

#crear un programa que muestre los 8 primeros numeros pares
contador=0
for n in range(1,17):
    if n%2==0:
    contador+=1
    print(f"(n) es par numero (contador)")

 #crear un programa que pida al usuario escribir una oracion y mostrar por terminal la cantidad de vocales "a" que tiene esa oracion
 oracion = input("escribe una oracion: ")
 contador_vocales = 0
 vocales = ´a´ 
 for letra in oracion:
    if lentra.islower() and letra in vocales:
    contrador_vocales += 1
    print("la oracion tiene", contador_vocales, "vocales en minusculas.")
    oracion:str=input("escribe una oracion: ")
    contador:int=0
    for n in range(0,len(oracion)):
        if oracion[n]=="a"
    contador-contador+1
    contador+=1
    print(f"la cantidad de letras que tengo es (contador)")
    for n in "aeiou":
    print(n)
    for ind_vocal,let_vocal in enumerate("aeiou"):
    print(f"la cantidad de letras a que tengo es (contador)")

#crear un programa que me cuente la cantidad de comas que me muestre sus indices, ojo tiene que pedir al usuario
oracion:str= input("escribe una oracion: ")
contador:int=0
for indice,letra in enumerate(oracion):
    if letra == ",":
    print(f"su indice es (indice)")
    contador+=1
    print(f"la cantidad de comes es (contador)")

#escribir un programa que me pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido(desde 1 hasta su edad actual)
edad:int=int(input("¿cuantos años tienes? "))
for e in range(edad):
    print("has cumplido " + str(e+1) + "edad")

#crear un programa que me pida el nombre de tres personas y guarde en una variable global la ultima letras de su nombre.
#mostrar por pantalla a variable global con las tres ultimas letras del nombre de cada persona
# Variable global para almacenar las últimas letras de los nombres
ultimas_letras = ""
# Pedir al usuario el nombre de tres personas
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    ultima_letra = nombre[-1]  # Obtener la última letra del nombre
    ultimas_letras += ultima_letra  # Concatenar la última letra a la variable global
# Mostrar por pantalla las últimas letras de los nombres de las tres personas
print("Últimas letras de los nombres de las tres personas:")
for letra in ultimas_letras:
    print(letra)
