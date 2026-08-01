class Habitacion:
    def __init__(self, numero, tipo, precio_por_noche):
        self.numero = numero
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche
        self.estado = "Disponible"
        self.huesped = None
        self.noches = 0
        
    def reservar(self, huesped, noches):
        if self.estado == "Ocupada":
            print("La habitacion ya esta ocupada")
            return False
    
        if noches > 0: # Aqui huesped y noches deben de ir en el if no afuera
        # el parametro noches al cambiar es el que debe condicionarse
        #si usara self.noches pues siempre seria 0    
            self.huesped = huesped
            self.noches = noches
            self.estado = "Ocupada"
            print("Se realizo correctamente la reserva")
            return True
        else:
            print("Las noches deben de ser mayores a 0")
            return False
        
    def calcular_total(self):
        if self.estado == "Disponible":
            return 0
        return self.precio_por_noche * self.noches
    
    def liberar(self, pago):
        if self.estado == "Ocupada":
            total = self.calcular_total()
            print(f"El huesped debe de pagar {total}")
            
            resultado = pago - int(total)
            if resultado < 0:
                print(f"El huesped no pago el total de las noches debe {abs(resultado)}")
                return 0 #Me falto el retorno aqui
            elif resultado == 0:
                self.estado = "Disponible"
                self.huesped = None
                self.noches = 0
                
                return total
            
            elif resultado > 0:
                self.estado = "Disponible"
                self.huesped = None
                self.noches = 0
                print(f"Le debemos {resultado} al huespued")
                
                return total
            
        print("La habitacion no esta ocupada")
        return 0
            
    def __str__(self):
        if self.estado == "Disponible":
            return f"Habitacion: {self.numero} | Tipo: {self.tipo} | Precio: {self.precio_por_noche} | Estado: {self.estado}"
        else:
            return f"Habitacion: {self.numero} | Tipo: {self.tipo} | Precio: {self.precio_por_noche} | Estado: {self.estado} | Huesped: {self.huesped} | Noches: {self.noches}"
    
class Hotel:
    def __init__(self):
        self.habitaciones = []
        self.ingresos = 0
        
    def agregar_habitacion(self, habitacion):
        for cuarto in self.habitaciones:
            if cuarto.numero == habitacion.numero:
                print("Son la misma habitacion")
                return False
            
        self.habitaciones.append(habitacion) #Tengo que guardar el parametro de cuarto
        print("Cuarto guardado correctamente")
        return True
    
    def buscar_habitacion(self, numero):
        for cuarto in self.habitaciones:
            if cuarto.numero == numero:
                print("La habitacion si existe")
                return cuarto
            
        return None
    
    def mostrar_habitaciones(self):
        if len(self.habitaciones) == 0: # Error en nombre de la lista
            print("No hay habitaciones registradas")
            return None
        
        for habitacion in self.habitaciones:
            print(habitacion)
            
    def mostrar_disponibles(self):
        hay_habitaciones = False
        
        for habitacion in self.habitaciones:
            if habitacion.estado == "Disponible":
                print(habitacion)
                hay_habitaciones = True
        
        if not hay_habitaciones:
            print("No hay habitaciones disponibles")
            return False
        
        return True
    
    def mostrar_ocupadas(self):
        
        hay_ocupadas = False
        
        for habitacion in self.habitaciones:
            if habitacion.estado == "Ocupada":
                print(habitacion)
                hay_ocupadas = True
                
        if not hay_ocupadas:
            print("No hay habitaciones ocupadas")
            return False
        
        return True
                
    def reservar_habitacion(self, numero, huesped, noches):
        habitacion_disponible = self.buscar_habitacion(numero)
        
        if habitacion_disponible is not None:
            print(f"Se encontro la habitacion {habitacion_disponible}")
            #Reservar puede fallar porque la habitacion esta ocupada 
            resultado = habitacion_disponible.reservar(huesped, noches)
            return resultado
        else:
            print("No se encontro la habitacion")
            return False
        
    def liberar_habitacion(self, numero, pago):
        habitacion_existe = self.buscar_habitacion(numero)
        
        if habitacion_existe is not None:
            total_cobrado = habitacion_existe.liberar(pago)
            
            if total_cobrado > 0:
                self.ingresos = self.ingresos + total_cobrado
                return True
            
        return False
    
    def mostrar_resumen(self):
        disponibles = 0
        ocupadas = 0
        
        for habitacion in self.habitaciones:
            if habitacion.estado == "Disponible":
                disponibles += 1
                
            else:
                ocupadas += 1
                
        cantidad_total_habitaciones = disponibles + ocupadas
        print(f"La cantidad de habitaciones del hotel es de {cantidad_total_habitaciones}")
        
        ingresos_totales = self.ingresos
        
        print(f"Total de habitaciones: {cantidad_total_habitaciones}")
        print(f"Habitaciones disponibles: {disponibles}")
        print(f"Habitaciones ocupadas: {ocupadas}")
        print(f"Ingresos totales: ${ingresos_totales:.2f}")
        
mi_hotel = Hotel()

while True:
    print("Menu")
    print("1) Registrar habitacion")
    print("2) Mostrar todas las habitaciones")
    print("3) Reservar habitacion")
    print("4) Liberar habitacion")
    print("5) Mostrar habitaciones disponibles")
    print("6) Mostrar habitaciones ocupadas")
    print("7) Mostrar resumen del hotel")
    print("8) Salir")
    
    try:
        opcion = int(input("Ingrese un numero: "))
    except ValueError:
        print("Opcion no valida solo numeros")
        continue
        
    if opcion < 1 or opcion > 8:
        print("La opcion se sale de los limites")
        continue
    
    match opcion:
        case 1:
            numero = int(input("Ingrese el numero de la habitacion: "))
            tipo = input("Ingrese el tipo de la habitacion: ")
            noche = input("Ingrese el cobro por noche de la habitacion")
            
            habitacion = Habitacion(numero, tipo, noche)
            
            mi_hotel.agregar_habitacion(habitacion)
        case 2:
            mi_hotel.mostrar_habitaciones()
        case 3:
            try:
                numero = int(input("Ingrese la habitacion que quiere reservar: "))
                huesped = input("Ingrese el nombre del huesped")
                noches = int(input("Ingrese las noches de estancia"))
            except ValueError:
                print("Numero de habitacion y noches deben de ser enteros")
                continue
            
            reservada = mi_hotel.reservar_habitacion(numero, huesped, noches)
            
            if reservada:
                habitacion = mi_hotel.buscar_habitacion(numero)
                total = habitacion.calcular_total()
                print(f"El total de la estancia es {total}")
                
        case 4:
            try:
                numero = int(input("Ingrese la habitacion que quiere liberar: "))
                pago = int(input("Ingrese la cantidad a pagar: "))
            except ValueError:
                print("Ingrese valores numericos: ")
                continue
            
            liberada = mi_hotel.liberar_habitacion(numero, pago)
            
            if not liberada:
                print("No fue posible liberar la habitacion")
        case 5:
            mi_hotel.mostrar_disponibles()
        case 6:
            mi_hotel.mostrar_ocupadas()
        case 7:
            mi_hotel.mostrar_resumen()
        case 8: 
            break