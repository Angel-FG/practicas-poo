class Bicicleta:
    def __init__(self, codigo, tipo, precio_por_hora):
        self.codigo = codigo
        self.tipo = tipo
        self.precio_por_hora = precio_por_hora
        self.estado = "Disponible"
        self.cliente = None
        # None 
        #Self.clientes = clientes
        # Jose
        self.horas = 0
        # self.horas = horas
        #     0      = 10  
        
    def rentar(self, cliente, horas):
        if self.estado == "Rentada":
            print("La Bicileta ya esta rentada")
            return False
        
        if horas <= 0:
            print("La bici no fue usada")
            return False
        
        if self.estado == "Disponible":
            self.cliente = cliente
            self.horas = horas
            self.estado = "Rentada"
            return True
        
    def metodo_calcular_total(self):
        if self.estado == "Disponible":
            return 0
        
        return self.precio_por_hora * self.horas
        # 100
    def devolver(self, pago):
        if self.estado == "Disponible":
            return 0
        
        if self.estado == "Rentada":
            total = self.metodo_calcular_total()
             # 100
             
        if pago <= 0:
            print("No se puede tener valores menores o iguales a 0")
            return 0
            
        if pago < total:
        # Total = 100 pago = 60         
            deuda = total - pago
            print(f"Falta dinero {deuda}")
            self.estado = "Rentada"
            return 0 #No fue posible la devolucion
        
        elif pago == total:
            print("El usuario pago todo el total")
            self.estado = "Disponible"
            self.cliente = None
            self.horas = 0
            return total

        elif pago > total:
            nuevo_cambio = pago - total
            self.estado = "Disponible"
            self.cliente = None
            self.horas = 0
            print(f"El usuario {self.cliente} dio un pago de mas su cambio sera de {nuevo_cambio}")
            return total
    
    def __str__(self):
        if self.estado == "Disponible":
            return f"Código: {self.codigo} | Tipo: {self.tipo} | Precio por hora: {self.precio_por_hora} | Estado: {self.estado}"
        else:
            return f"Código: {self.codigo} | Tipo: {self.tipo} | Precio por hora: {self.precio_por_hora} | Estado: {self.estado} | Cliente: {self.cliente} | Horas: {self.horas}"
        
class TiendaBicicletas:
    def __init__(self):
        self.bicicleta = []
        self.ingresos = 0
        
    def agregar_bicicleta(self, bicicleta):
        for bicicletas in self.bicicleta:
            if bicicletas.codigo == bicicleta.codigo:
                print("La bicicleta ya existe")
                return False
            
        self.bicicleta.append(bicicleta)
        return True
    
    def buscar_bicicleta(self, codigo):
        for buscar_bicicletas in self.bicicleta:
            if buscar_bicicletas.codigo == codigo:
                return buscar_bicicletas
            
        return None
    
    def mostrar_bicicletas(self):
        if len(self.bicicleta) == 0:
            print("No hay bicicletas para mostrar")
        
        for mostrar_bicicleta in self.bicicleta:
            print(mostrar_bicicleta)
            
    def mostrar_disponibles(self):
        hay_disponibles = False
        
        for buscar_bici in self.bicicleta:
            if buscar_bici.estado == "Disponible":
                print(buscar_bici)
                hay_disponibles = True
                
        if not hay_disponibles:
            print("No hay bicis disponibles en este momento")
            return False
        
        return True
    
    def mostrar_rentadas(self):
        hay_rentadas = False
        
        for rentadas in self.bicicleta:
            if rentadas.estado == "Rentada":
                print(rentadas)
                hay_rentadas = True
            
        if not hay_rentadas:
            print("No hay bicis rentadas. Todas estan disponibles")
            return False
        
        return True
    
    def rentar_bicicleta(self, codigo, cliente, horas):
        buscar_bici = self.buscar_bicicleta(codigo)
        if buscar_bici == None:
            return False
        encontrada = buscar_bici.rentar(cliente, horas)
        return encontrada
    
    def devolver_bicicleta(self, codigo, pago):
        buscar_bici = self.buscar_bicicleta(codigo)
        
        if buscar_bici == None:
            return False
        
        total_devuelto = buscar_bici.devolver(pago)
        
        if total_devuelto >= 0:
            self.ingresos += total_devuelto
            return total_devuelto
                
    def mostrar_resumen(self):
        contador_disponibles = 0
        contador_rentadas = 0
        
        for bicis in self.bicicleta:
            if bicis.estado == "Disponible":
                contador_disponibles += 1
            else:
                contador_rentadas += 1
        
        ingresos_acumulados = self.ingresos
        print(contador_disponibles)
        print(contador_rentadas)
        print(f"Hay un total de {len(self.bicicleta)} Bicis en total")
        print(ingresos_acumulados)
        
mi_tienda = TiendaBicicletas()


while True:
    print("Tienda de Bicicletas")
    print("1) Registrar bicicleta")
    print("2) Mostrar todas las bicicletas")
    print("3) Rentar bicicleta")
    print("4) Devolver bicicleta")
    print("5) Mostrar bicicletas disponibles")
    print("6) Mostrar bicicletas rentadas")
    print("7) Mostrar resumen")
    print("8) Salir")
    
    try:
        opcion = int(input("Ingrese la opcion que desee: "))
    except ValueError:
        print("Solo se permiten numeros")
        continue
    
    if opcion < 0 or opcion > 8:
        print("Tiene que ser solo numeros del 1 al 8")
        continue
    
    match opcion:
        case 1:
            codigo = int(input("Ingrese el codigo de la bici: "))
            tipo = input("Ingrese el tipo de la bici: ")
            precio_por_hora = int(input("Ingrese el precio por hora: "))
            Nueva_bici = Bicicleta(codigo, tipo, precio_por_hora)
            
            mi_tienda.agregar_bicicleta(Nueva_bici)
        case 2:
            mi_tienda.mostrar_bicicletas()
        case 3:
            codigo =int(input("Ingrese el codigo de la bici: "))
            
            bici = mi_tienda.buscar_bicicleta(codigo)
            
            if bici != None:
                cliente = input("Ingrese el nombre del cliente")
                horas = int(input("Ingrese las horas que se usara la bici: "))
                mi_tienda.rentar_bicicleta(codigo, cliente, horas)
                
        case 4:
            try:
                codigo = int(input("Ingrese el codigo de la bici: "))
                pago = int(input("Ingrese el pago de la bicicleta: "))
            except ValueError:
                print("Solo pueden ser numeros")
                
            devuelta = mi_tienda.devolver_bicicleta(codigo, pago)
            bici = mi_tienda.buscar_bicicleta(codigo)
            total = bici.metodo_calcular_total()
            #Almacenar el retorno True or False en la variable devuelta
            print(f"El total de la bici es de {total}")
            if devuelta is not False:
                dinero = total - devuelta
                print(f"El pago de la bicicleta es {dinero}")
            
        case 5:
            mi_tienda.mostrar_disponibles()
        case 6:
            mi_tienda.mostrar_rentadas()
        case 7:
            mi_tienda.mostrar_resumen()
        case 8:
            break

        
        
        