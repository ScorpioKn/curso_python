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

#crear un programa que muestre por terminal la siguiente figura:
# Función para imprimir el triángulo con las cinco vocales
def imprimir_triangulo_vocales():
    vocales = ['a', 'e', 'i', 'o', 'u']
    espacio = " "
    for i in range(5):
        linea = espacio * (5 - i - 1)  # Espacios en blanco antes de la vocal
        for j in range(i + 1):
            linea += vocales[j] + espacio  # Agregar vocal y espacio
        print(linea)
# Llamar a la función para imprimir el triángulo con las vocales
imprimir_triangulo_vocales()