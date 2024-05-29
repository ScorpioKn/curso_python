# el usuario tiene un grass el cual administra de manera manual, el usuario necesita que se automatize el proceso de la reserva y el pago del alquiler, para lo cual solicita los siguientes casos de uso.
el usuario podra ver la lista de horarios disponibles.
el usuario podria reservar en uno de los horarios disponibles.
el usuario podra pagar por el alquiler de la reserva realizada.
el usuario podra verificar su alquiler el cual le mostrara los detalles como la fecha, hora y costo del alquiler que realizo.
# Listas de horarios disponibles
horarios_disponibles = ["10:00 - 12:00", "14:00 - 16:00", "18:00 - 20:00"]

# Mostrar listas de horarios disponibles
print("Horarios disponibles:")
for horario in horarios_disponibles:
    print(horario)

# Solicitar al usuario que elija un horario
horario_elegido = input("Seleccione un horario de la lista: ")

# Realizar la reserva en el horario elegido
reserva_realizada = True  # Simulación de reserva exitosa

# Verificar si la reserva se realizó con éxito
if reserva_realizada:
    print("Reserva realizada con éxito.")
    # Precio del alquiler
    costo_alquiler = 50  # Costo fijo por reserva
    
    # Pagar el alquiler
    pago_realizado = True  # Simulación de pago exitoso
    
    # Verificar el alquiler
    if pago_realizado:
        print("Pago del alquiler realizado.")
        print("Detalles del alquiler:")
        print(f"Fecha y hora: {horario_elegido}")
        print(f"Costo: ${costo_alquiler}")
    else:
        print("Error en el pago del alquiler.")
else:
    print("Error en la reserva del horario.")