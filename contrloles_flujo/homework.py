# Programa para calcular el precio de entrada a una sala de juegos según la edad del cliente

# Solicitar la edad del cliente al usuario
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada según la edad
if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

# Mostrar el precio de la entrada al cliente
print(f"El precio de la entrada para un cliente de {edad} años es: {precio_entrada} soles.")

segundo ejercicio

# Programa para mostrar una palabra ingresada por el usuario 10 veces usando un bucle while

# Solicitar al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Inicializar el contador
contador = 0

# Mostrar la palabra 10 veces
while contador < 10:
    print(palabra)
    contador += 1

tercer ejercicio

# Programa para mostrar todos los números impares desde 1 hasta un número entero positivo ingresado por el usuario

# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Inicializar el contador
contador = 1

# Mostrar los números impares hasta el número ingresado
print("Números impares hasta", numero, ":")

while contador <= numero:
    if contador % 2 != 0:
        if contador != 1:
            print(",", end=" ")
        print(contador, end="")
    contador += 1

    cuarto ejercicio

# Programa para mostrar la tabla de multiplicar del 1 al 10

# Iterar sobre los números del 1 al 10
for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    
    # Calcular y mostrar la tabla de multiplicar
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()  # Salto de línea entre tablas

quinto programa

# Programa para mostrar las letras de una palabra introducida por el usuario empezando por la última

# Solicitar al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Obtener la longitud de la palabra
longitud = len(palabra)

# Inicializar el índice
indice = longitud - 1

# Mostrar las letras de la palabra empezando por la última
print("Letras de la palabra introducida empezando por la última:")
while indice >= 0:
    print(palabra[indice])
    indice -= 1

sexto programa
# Programa para mostrar un triángulo rectángulo con asteriscos según el número entero ingresado por el usuario

# Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Mostrar el triángulo rectángulo
for i in range(1, numero + 1):
    print("*" * i)

    septimo programa

# Programa para contar el número de veces que una letra aparece en una frase ingresada por el usuario

# Solicitar al usuario una frase y una letra
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Inicializar el contador de apariciones de la letra
contador = 0

# Contar el número de veces que la letra aparece en la frase
indice = 0
while indice < len(frase):
    if frase[indice] == letra:
        contador += 1
    indice += 1

# Mostrar el resultado al usuario
print(f"La letra '{letra}' aparece {contador} veces en la frase.")

octavo programa

# Programa para mostrar la primera, letra del medio y última letra de una palabra ingresada por el usuario

# Solicitar al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Obtener la longitud de la palabra
longitud = len(palabra)

# Calcular el índice de la letra del medio
indice_medio = longitud // 2

# Mostrar la primera, letra del medio y última letra separadas por comas
primera_letra = palabra[0]
letra_medio = palabra[indice_medio]
ultima_letra = palabra[-1]

print(f"{primera_letra}, {letra_medio}, {ultima_letra}")

noveno programa

# Programa para verificar si los números introducidos son mayores que el anterior

# Solicitar al usuario la cantidad de números a introducir
cantidad_numeros = int(input("Ingrese cuántos números va a introducir: "))

# Inicializar la variable para almacenar el número anterior
anterior = None

# Pedir y verificar los números introducidos
while cantidad_numeros > 0:
    numero = float(input("Ingrese un número: "))
    
    if anterior is not None and numero <= anterior:
        print("El número introducido no es mayor que el anterior.")
    
    anterior = numero
    cantidad_numeros -= 1

decimo programa

# Programa para contar el número de veces que una letra aparece en una frase ingresada por el usuario

# Solicitar al usuario una frase y una letra
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

# Inicializar el contador de apariciones de la letra
contador = 0

# Contar el número de veces que la letra aparece en la frase
for caracter in frase:
    if caracter == letra:
        contador += 1

# Mostrar el resultado al usuario
print(f"La letra '{letra}' aparece {contador} veces en la frase.")

onceavo programa

# Programa para calcular la suma de números introducidos por el usuario

# Solicitar al usuario la cantidad de números a introducir
cantidad_numeros = int(input("Ingrese cuántos números va a introducir: "))

# Inicializar la variable para almacenar la suma
suma = 0

# Pedir y sumar los números introducidos
while cantidad_numeros > 0:
    numero = float(input("Ingrese un número: "))
    suma += numero
    cantidad_numeros -= 1

# Mostrar la suma de los números introducidos
print(f"La suma de los números introducidos es: {suma}")

doceavo programa

# Programa para contar cuántos números negativos se han introducido

# Solicitar al usuario la cantidad de números a introducir
cantidad_numeros = int(input("Ingrese cuántos números va a introducir: "))

# Inicializar el contador de números negativos
contador_negativos = 0

# Pedir los números e identificar los negativos
while cantidad_numeros > 0:
    numero = float(input("Ingrese un número: "))
    
    if numero < 0:
        contador_negativos += 1
    
    cantidad_numeros -= 1

# Mostrar la cantidad de números negativos introducidos
print(f"Ha introducido {contador_negativos} número(s) negativo(s).")

decimo tercer ejercicio

# Calculadora interactiva que realiza operaciones según la elección del usuario

# Inicializar la calculadora
encendida = True

while encendida:
    # Solicitar al usuario los datos A, B y la operación a realizar
    A = float(input("Ingrese el valor de A: "))
    B = float(input("Ingrese el valor de B: "))
    operacion = int(input("Elija la operación a realizar (1: raíz cuadrada de la suma, 2: división, 3: fórmula especial): "))

    # Realizar la operación seleccionada
    if operacion == 1:
        resultado = (A + B) ** 0.5
    elif operacion == 2:
        if B != 0:
            resultado = A / B
        else:
            print("Error: No se puede dividir por 0.")
            continue
    elif operacion == 3:
        resultado = (A * B) / 2.5
    else:
        print("Operación no válida.")
        continue

    # Mostrar el resultado de la operación
    print("El resultado de la operación es:", resultado)

    # Preguntar al usuario si desea apagar la calculadora
    apagar = input("¿Desea apagar la calculadora? (Escriba 'SAL' para salir): ")
    if apagar == "SAL":
        encendida = False
        
decimo cuarto ejercico

# Programa para simular el desbloqueo de la pantalla de un móvil con un PIN secreto

# PIN secreto para desbloquear la pantalla
PIN_SECRETO = "1234"

# Inicializar el contador de intentos
intentos = 3

# Simular el proceso de desbloqueo
while intentos > 0:
    # Solicitar al usuario que ingrese el PIN
    pin_ingresado = input("Ingrese el PIN para desbloquear la pantalla: ")
    
    # Verificar si el PIN ingresado es correcto
    if pin_ingresado == PIN_SECRETO:
        print("Login correcto.")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"PIN incorrecto. Le quedan {intentos} intento(s).")
        else:
            print("Llamando a la policía.")

decimo quinto ejercicio

# Programa para generar la sucesión de Fibonacci

# Inicializar los dos primeros números de la sucesión
num1 = 0
num2 = 1

# Mostrar los dos primeros números
print(num1)
print(num2)

# Generar el resto de la sucesión
for _ in range(10):  # Generar 10 números adicionales
    siguiente_num = num1 + num2
    print(siguiente_num)
    num1 = num2
    num2 = siguiente_num

ejercicio 16

# Programa para gestionar una lista de tareas pendientes

# Inicializar la lista de tareas pendientes
tareas_pendientes = []

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Salir")

# Ciclo interactivo para gestionar las tareas
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nueva_tarea = input("Ingrese la nueva tarea: ")
        tareas_pendientes.append(nueva_tarea)
        print("Tarea agregada correctamente.")
    elif opcion == "2":
        if tareas_pendientes:
            print("Tareas pendientes:")
            for i, tarea in enumerate(tareas_pendientes):
                print(f"{i + 1}. {tarea}")
            tarea_completada = int(input("Ingrese el número de la tarea completada: "))
            if 1 <= tarea_completada <= len(tareas_pendientes):
                del tareas_pendientes[tarea_completada - 1]
                print("Tarea marcada como completada.")
            else:
                print("Número de tarea inválido.")
        else:
            print("No hay tareas pendientes para marcar como completadas.")
    elif opcion == "3":
        if tareas_pendientes:
            print("Tareas pendientes:")
            for i, tarea in enumerate(tareas_pendientes):
                print(f"{i + 1}. {tarea}")
        else:
            print("No hay tareas pendientes.")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

ejercicio 17

# Programa simulador de cajero automático

# Saldo inicial
saldo = 1000

# Ciclo interactivo para simular el cajero automático
while True:
    print("\nMenú de opciones:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Su saldo actual es: {saldo} soles.")
    elif opcion == "2":
        monto_deposito = float(input("Ingrese el monto a depositar: "))
        saldo += monto_deposito
        print(f"Se ha depositado {monto_deposito} soles. Su saldo actual es: {saldo} soles.")
    elif opcion == "3":
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        if monto_retiro <= saldo:
            saldo -= monto_retiro
            print(f"Se ha retirado {monto_retiro} soles. Su saldo actual es: {saldo} soles.")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

ejercicio 18

# Programa para solicitar y verificar una contraseña

# Solicitar la primera contraseña al usuario
contrasena1 = input("Ingrese la contraseña: ")

# Solicitar la segunda contraseña y verificar si coincide con la primera
while True:
    contrasena2 = input("Confirme la contraseña: ")
    
    if contrasena2 == contrasena1:
        print("Las contraseñas coinciden. Contraseña establecida con éxito.")
        break
    else:
        print("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")