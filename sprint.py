""""● Seleccione cuatro de las clases de su diagrama. Privilegie las clases que tienen algún tipo de
herencia, Debe desarrollarlo en un script, plasmando la dinámica entre clases y respectivas
herencias.
● Identifique y diseñe claramente sus respectivos métodos y atributos. Las clases deben heredar
atributos-métodos utilizando la función super().
● Asegúrese de manejar al menos 2 posibles errores, según los contenidos revisados.
● Privilegie la clase usuario (o equivalente). En este sentido debe almacenar la información de los
usuarios en un archivo JSON o CSV según estimen conveniente.
Recuerde comentar debidamente el código, para facilitar su comprensión."""""


""" el sistema permite realizar reservaciones a eventos, las reservaciones 
 se pueden hacer directamente por el cliente en el lugar del evento, se pueden comprar las entradas a través de
 ticketers o en la agencia creadora del evento



"""
import json
import os

class Evento:
    def __init__(self, nombre_evento, ubicacion, fecha_evento, tipo, capacidad, valor):
        self.nombre_evento = nombre_evento
        self.ubicacion = ubicacion
        self.fecha_evento = fecha_evento
        self.tipo = tipo
        self.capacidad = capacidad
        self.valor = valor    


class Cliente:
    cargo_extra=1.0
    def __init__(self,nombre_pasajero,rut,edad, fono_contacto, email):
        self.nombre_pasajero=nombre_pasajero
        self.rut=rut
        self.edad=edad
        self.fono_contacto=fono_contacto
        self.email=email 

    def hacer_reserva (self):
        
                
        with open("eventos.json") as f:
            data = json.load(f)
        evento_a_reservar=input("Indique nombre del evento: ")
        encontrado = False
        for evento in data["eventos"]:
            if  evento["nombre_evento"] == evento_a_reservar:
                try:
                    reservas_a_realizar=int(input("Indique número de reservas: "))
                except:
                    print("Número no valido")
                if evento["capacidad"]>= int(reservas_a_realizar):
                    nuevo_valor =(evento["valor"]*self.cargo_extra)*int(reservas_a_realizar)
                    print(f"su resevar fue aceptada por un total de {nuevo_valor}")
                    
                    evento["capacidad"] -= int(reservas_a_realizar)
                    with open("eventos.json", "w") as f:
                        #Guardar las reservar realizadas en un archivo con el nombre del evento
                        json.dump(data,f)
                    encontrado= True
                    break
                else:
                    print("La capacidad del evento fue superada no podemos realizar su reserva.") 
        if not encontrado :
            print("Evento no entonrado")
# Clase Tiquetera vende tickets para cualquier evento

class Tiquetera(Cliente):
    cargo_extra=1.2
    def __init__(self,nombre_pasajero,rut,edad, fono_contacto, email,nombre_evento):
        super().__init__(nombre_pasajero,rut,edad, fono_contacto, email)
        self.nombre_evento=nombre_evento

    def hacer_reserva (self):
        super.hacer_reserva()
    
# Clase Agencia puede crear eventos y vender tickets solo para eventos que ella crea
class Agencia(Cliente):  
    cargo_extra=1.1
    def __init__(self,nombre_pasajero,rut,edad, fono_contacto, email,nombre_evento):
        super().__init__(nombre_pasajero,rut,edad, fono_contacto, email)
        self.nombre_evento=nombre_evento

    def hacer_reserva (self):
        super.hacer_reserva()
    
    #crear eventos
    def crear_evento(self):
        nombre_evento = input("Ingrese el nombre del evento: ")
        ubicacion = input("Ingrese la ubicación del evento: ")
        fecha_evento = input("Ingrese la fecha del evento: ")
        tipo = input("Ingrese el tipo de evento: ")
        capacidad = input("Ingrese la capacidad del evento: ")
        valor = input("Ingrese el valor del evento: ")

        # Abrir el archivo JSON y agregar el nuevo evento al diccionario de eventos
        with open("eventos.json", "r") as f:
            data = json.load(f)
            eventos = data["eventos"]
            eventos.append({
                "nombre_evento": nombre_evento,
                "ubicacion": ubicacion,
                "fecha_evento": fecha_evento,
                "tipo": tipo,
                "capacidad": capacidad,
                "valor": valor
            })

        # Guardar los cambios en el archivo JSON
        with open("eventos.json", "w") as f:
            json.dump(data, f)

        print("Evento creado exitosamente!")

   
        


with open('clientes.json') as f:
    data = json.load(f)
for usuario in data['clientes']:
    if usuario['rut'] == '11.111.111-1':
        # Crear una instancia de la clase Cliente con los valores correspondientes del usuario encontrado
        cliente1 = Cliente(usuario['nombre_pasajero'], usuario['rut'], usuario['edad'], usuario['fono_contacto'], usuario['email'])

        cliente1.hacer_reserva()
        