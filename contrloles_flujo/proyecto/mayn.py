horarios_disponibles=["06:00- 08:00","13:00-15:00","16:00-18:00","19:00-21:00"]
print("horas_disponibles: ")
for horarios in horarios_disponibles:
    print(horarios)
horarios_seleccionada=input("selecione un horario de la lista: ")
reserva_lista=True
if reserva_lista:
    print("reserva realizada con exito.")
    costo_alquiler=50
    pago_realizado= True
    if pago_realizado:
        print("pago del alquiler realizado.")
        print("detalles del alquiler.")
        print(f"fecha y hora: {horarios_seleccionada}")
        print(f"costo: $ {costo_alquiler}")
    else:
        print("error en el pago del alquiler")
        print("error en la reserva del horario.")