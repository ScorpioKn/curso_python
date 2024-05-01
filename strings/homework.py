# Solicitar al usuario que ingrese su nombre completo
nombre_completo = input("Por favor, ingresa tu nombre completo: ")

# Mostrar el nombre completo del usuario tres veces en pantalla
for _ in range(3):
    print(nombre_completo)



    # Solicitar al usuario que ingrese su nombre y sexo
nombre = input("Por favor, ingresa tu nombre: ")
sexo = input("Ahora, ingresa tu sexo (M para masculino, F para femenino): ")

# Convertir el nombre a minúsculas para facilitar la comparación
nombre = nombre.lower()

# Determinar el grupo al que pertenece el alumno
if (sexo == 'F' and nombre < 'm') or (sexo == 'M' and nombre > 'n'):
    grupo = 'A'
else:
    grupo = 'B'

# Mostrar por pantalla el grupo al que pertenece el alumno
print("El grupo al que perteneces es:", grupo)