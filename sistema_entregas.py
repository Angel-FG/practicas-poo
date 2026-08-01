"""
Vamos a crear una clase Pedido para gestionar rutas de entrega.

Atributos: Nombre del cliente, zona de entrega, total a cobrar y estado (que nazca siempre como "Pendiente").

Métodos: Una función entregar_paquete() que cambie el estado a "Entregado" y registre el pago en efectivo o transferencia.
"""

class Pedido():
    def __init__(self, nombre, zona, cobro):
        self.nombre = nombre
        self.zona = zona
        self.cobro = cobro
        self.estado = "pendiente"
        
    def __str__(self):
        return (
            f"Cliente: {self.nombre} | "
            f"Zona: {self.zona} | "
            f"Cobro pendiente: ${self.cobro:.2f} | "
            f"Estado: {self.estado}"
        )
        
    def entregar_paquete(self, pago):
        if pago > self.cobro:
            cambio = pago - self.cobro
            print(f"La clienta {self.nombre} de la zona {self.zona} pago su pedido por un total de {self.cobro} y quedamos debiendole {cambio}")
            self.cobro = 0
            self.estado = "Entregado"
            
        
        elif pago == self.cobro:
            self.cobro = pago - self.cobro
            self.cobro = 0
            self.estado = "Entregado"
            print(f"La clienta {self.nombre} de la zona {self.zona} pago su pedido y no quedo debiendo")
            
        else:
            self.cobro -= pago 
            print(f"La clienta {self.nombre} de la zona {self.zona} nos dio un abono de su pedido le resto {self.cobro}")
            
class Ruta():
    def __init__(self):
        self.pedido_dia = []
    
    def agregar_ruta(self, pedido):
        self.pedido_dia.append(pedido)
        print(f"Se ha guardado correctamente el pedido {pedido}")

    def pendientes(self):
        for pedidos in self.pedido_dia:
            print(pedidos)
            
            
mi_ruta = Ruta()

while True:
    print("Bienvenido a la gestion de rutas")
    print("1) Registrar nuevo pedido")
    print("2) Ver ruta completa")
    print("3) Cobrar un paquete")
    print("4) Salir")
    try:
        opcion = int(input("Seleccione una de las opciones: "))
        
        if opcion > 5:
            raise ValueError("Solo esta de 1 a 4")
        
    except ValueError:
        print("Incorrecto")
        
    match opcion:
        case 1:
            nombre = input("Ingrese su nombre: ")
            zona = input("Ingrese la zona donde vive: ")
            monto = float(input("Ingrese la cantidad a cobrar $: "))
            
            Nuevo_registro = Pedido(nombre, zona, monto)               
            
            mi_ruta.agregar_ruta(Nuevo_registro)
            
        case 2:
            mi_ruta.pendientes()
            
        case 3:
            nombre_buscar = input("Ingrese el nombre de la clienta: ")
            
            encontrado = False
            
            for pedido_actual in mi_ruta.pedido_dia:
                
                if pedido_actual.nombre.lower() == nombre_buscar.lower():
                    encontrado = True
                    print(f"Clienta encontrada deuda actual {pedido_actual.cobro}")

                    pago_recibido = float(input("Cuanto dinero dio la clienta? $"))
                    
                    pedido_actual.entregar_paquete(pago_recibido)
                    
                    break
            
            if not encontrado:
                print(f"No se encontro ningun pedido para la clienta {nombre_buscar}")
        case 4:
            break