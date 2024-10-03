# #crear una clase  banco sus atributos seran nombre apellidos deni numero de cuenrta
# #y saldo inicial
# #como metodos podremos hacer deposito retirar dinero y ver estado de cuenta
# class banco:
#     #atributos
#     def _init_(self,nombre,apellidos,dni,numero_de_cuenta,saldo_inicial):
#         self.nombre=nombre
#         self.apellidos=apellidos
#         self.dni=dni
#         self.numero_de_cuenta=numero_de_cuenta
#         self.saldo_inicial=saldo_inicial
#     #metodos
#     def deposito(self):
#         print("estoy depositando 120")
#     def retirar(self):
#         print("estoy retirando 120")
#     def get_status(self):
#         print("estoy viendo el get status actual de mi cuenta")
# mario=banco("mario","ramos lopez",7455125,787998,1220)
# print(mario.deposito())

class agencia:
    #atributos
    def _init_(self,nombre,apellidos,dni,numero_asiento,fecha_viaje):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.numero_asiento=numero_asiento
        self.fecha_viaje=fecha_viaje
    #metodos
    def ingresar_origen(self,lugar):
        print("estoy ingresando a mi destino:",lugar)
    def ingresar_destino(self):
        print("estoy ingresando mi retorno")
    def cancelar_viaje(self):
        print("estoy cancelando mi transporte ")
    def ver_estado_pasaje(self):
        print("estoy viendo el control de mi pasaje")
esteban=agencia("esteban","garriazo ramos",74124556,122,"2024-1-22")
print(esteban.ingresar_destino())
esteban.ingresar_origen("puquio")       
esteban=agencia("esteban","garriazo ramos"74124556,122"2024-1-22")
print(malu)                       