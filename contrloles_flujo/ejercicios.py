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

for i,letra in enumerate("aeiou"):
    print(letra * (i + 1))
    c