class Herramienta:
    def __init__(self, codigo, nombre, categoria, precio_por_dia):
        #Estos son atributos de la herramienta
         self.codigo = codigo
         self.nombre = nombre # El nombre de la herramienta
         self.categoria = categoria
         self.precio_por_dia = precio_por_dia
         self.estado = "Disponible"
         # Estis son parametros que se reciben
         self.cliente = None # El cliente se usa para saber que cliente es
         self.dias = 0
         
    def rentar(self, cliente, dias):
        if self.estado == "Rentada":
            print("La bici ya esta rentada")
        
        if dias <= 0:
            print("No se pueden recibir valores negativos o iguales a cero")
        
        self.cliente = cliente
        self.dias = dias
        self.estado = "Rentada"
        return True # La operacion funcion entonces se retorna un True
    
    def calcular_total(self):
        if self.estado == "Disponible":
            return 0
        return self.precio_por_dia * self.dias # Se retorna en True porque queremos saber el valor total
    
    def devolver(self, pago): #Ocupo el paramtro pago para saber cuanto pago el cliente
        if self.estado == "Disponible":
            print("La herramienta esta disponible no se puede devolver")
            return False # La accion no se completo devolver devolvera False
        if pago <= 0:
            print("No se aceptan pago iguales o menores a cero")
            return 0 # Retornamos el valor en 0 para no tener problemas de datatype
        
        total = self.calcular_total() #Llamamos al metodo de calcular total para no hacerlo manualmente y lo almacenamos en una variable
        #e.j self.precio_por_dia * self.dias = 200, total almacena 200
        
        if pago < total:
            #  70    = 100      30 
            faltante = total - pago
            print(f"Falta dinero. El dinero que falta es {faltante}")
            self.estado = "Rentada" # La herramienta se mantiene rentada ya que no se ha terminado de pagar
            return 0 # No se registran ingresos
        elif pago == total:
            print("El pago fue completado")
            
        elif pago > total:
            # 100  =  300    200  evitamos que haya valores negativos
            cambio = pago - total
            print(f"La herramienta ha sido pagada en su totalidad, le devolvemos cambio el cambio es de {cambio}")
        
        #Suponiendo que la condicion sea una de los dos elif entonces saltarian despues de hacer lo que hacen dentro a estas dos lineas de aqui
        #Se dice de liberar por completo la herramienta lo que es cambiar su estado, borrar al cliente y reiniciar los dias a cero
        self.estado = "Disponible"
        self.cliente = None
        self.dias = 0
        return total
    
    def __str__(self):
        if self.estado == "Disponible":
            return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Categoria: {self.categoria} | Precio: {self.precio_por_dia} | Estado: {self.estado}"
        else:
            return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Categoria: {self.categoria} | Precio: {self.precio_por_dia} | Estado: {self.estado} | Cliente: {self.cliente} | Dias: {self.dias}"
        
class Taller:
    def __init__(self):
        self.herramientas = []
        self.ingresos = 0
        
    def agregar_herramienta(self, herramienta): #Los paramtros deben de pensarse como elementos que va a pasar el usuario
        #Se me olvido que se pasaba el parametro herramienta para ver si un elemento coincidia con el codigo de alguna herramienta
        for herramientaB in self.herramientas:
            if herramientaB.codigo == herramienta.codigo:
                print("Esa herramienta ya existe")
                return False #La herramienta no se agrego
        self.herramientas.append(herramienta) #Se almacena el valor en la lista como normalmente se hace
        print("Se ha guardado correctamente la herramienta")
        return True #Se registra que el metodo funciono
    
    def buscar_herramienta(self, codigo):
        for buscar in self.herramientas:
            if buscar.codigo == codigo:
                print("Se encontro el objeto")
                return buscar #En este caso no debemos de retornar True ya que lo que queremos es el objeto completo que es la herramienta
        return None #En este caso si no se encontro algun objeto entonces no va a retornar nada
    
    def mostrar_todas_las_herramientas(self):
        if len(self.herramientas) == 0: #Se registra la lista la cantidad de elementos que tiene si es igual a 0 pues no hay
            print("No hay herramientas guardadas")
        #Esta parte si no usaramos len se veria de la siguiente manera
        #for h in self.herramientas:
        #    if h == None:
        #        print("No hay herramientas")
        
        for herramientas in self.herramientas:
            print(herramientas)
            
    def herramientas_disponibles(self):
        hay_disponibles = False #Se inicializa la bandera en False ya que le decimos a la maquina que espere lo peor que no hay ninguna disponible
        
        for herramienta in self.herramientas:
            if herramienta.estado == "Disponible": #Si el estado de la herramienta es disponible entonces si hay herramientas disponibles
                print(herramienta)
                hay_disponibles = True #Cambia el estado de la bandera
        
        if not hay_disponibles:
            print("No hay bicicletas disponibles")
            return False #Si no hay ninguna bicicleta entonces el metodo fallo
        
        return True #En la parte de hayDisponibles el valor cambio a True pero es privado no retorna el metodo True por eso si la condicion se aplico el metodo retornara True
    
         
    def herramientas_rentadas(self):
        hay_rentadas = False #Se inicializa la bandera en False ya que le decimos a la maquina que espere lo peor que no hay ninguna disponible
        
        for herramienta in self.herramientas:
            if herramienta.estado == "Rentada": #Si el estado de la herramienta es disponible entonces si hay herramientas disponibles
                print(herramienta)
                hay_rentadas = True #Cambia el estado de la bandera
        
        if not hay_rentadas:
            print("No hay bicicletas rentadas")
            return False #Si no hay ninguna bicicleta entonces el metodo fallo
        
        return True    
    
    def rentar_herramienta(self, codigo, cliente, dias):
        buscar = self.buscar_herramienta(codigo) #Le pedimos al usuario ingresar un input donde le pediremos el codigo de la herramienta
        #con esto en mente el codigo pasara a este self y se lo llevara al metodo
        
        if buscar == None: #Si buscar devuelve None enotnces es que no se encontro ningun elemento con codigo, al final del metodo se puede ver que si no se encontro nada que devuelva None
            print("No existe ninguna herramienta con ese codigo")
            return False
            
        #Buscar en si devueleve el objeto completo, entonces devuelve el objeto con todos sus atributos
        objetoRentado = buscar.rentar(cliente, dias) #Rentar requiere de dos parametros adicionales y devolvera True
        return objetoRentado #Esta correcto se devuelve el objeto completo que en este caso guardara True
    
    def devolver_herramienta(self, codigo, pago):
        buscar = self.buscar_herramienta(codigo)
        
        if buscar == None:
            print("La herramienta no existe")
            return False
        
        #Aqui lo que hacemos es simplemente que el objeto completo entre al metodo de devolver, devolver ya tiene su logica entonces no hay que hacer nada mas
        ProcesarDevolucion = buscar.devolver(pago) #ProcesarDevolucion o devuelve 0 o devuelve un valor entero
        
        if ProcesarDevolucion <= 0: #Hacemos una doble verificacion
            self.ingresos = 0
            return 0
        
        #Lo que retorna devolver es el total entonces con eso en mente podemos tomar ProcesarDevolucion como un entero y lo añadimos a self.ingresos
        self.ingresos += ProcesarDevolucion
        
    def resumen_taller(self):
        cantidadDisponible = 0
        cantidadRentada = 0
        
        for herramienta in self.herramientas:
            if herramienta.estado == "Disponible":
                cantidadDisponible += 1
            else:
                cantidadRentada += 1
                
        totalIngresos = self.ingresos
        
        print(f"Total de herramientas es {len(self.herramientas)}")
        print(f"Total de herramientas disponibles {cantidadDisponible}")
        print(f"Total de herramientas rentadas {cantidadRentada}")
        print(f"Ingresos acumulados {totalIngresos}")

miTaller = Taller() #Inicializamos la clase taller ya que es una clase administadora

while True:
    print("Taller de herramientas")
    print("1) Registrar herramientas")
    print("2) Mostrar todas")
    print("3) Rentar")
    print("4) Devolver")
    print("5) Mostrar disponibles")
    print("6) Mostrar rentadas")
    print("7) Mostrar resumen")
    print("8) Salir") 
    
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Solo se aceptan valores numericos")
        continue
    
    if opcion < 1 or opcion > 8:
        print("Solo se pueden ingresar valores del 1 al 8")
        continue
    
    match opcion:
        case 1:
            #Lo que tenemos que hacer es crear inputs para que el molde que es la clase herramienta cree estas herramientas
            #Luego lo que haremos sera añadir estas herramientas a la lista de agregar herramientas
            #codigo, nombre, categoria, precio_por_dia
            codigo = int(input("Ingres el codigo de la herramienta: "))
            nombre = input("Ingrese el nombre de la herramienta: ")
            categoria = input("Ingrese la categoria de la herramienta: ")
            precioPorDia = int(input("Ingrese el precio por dia de la herramienta: "))
            
            herramientaCreada = Herramienta(codigo, nombre, categoria, precioPorDia) #El molde ya tiene los elementos y ya puede crear las herramientas
            
            #Ahora esa herramienta creada con ese molde lo agregamos a las herramientas
            guardado = miTaller.agregar_herramienta(herramientaCreada) #Simplemente le pasamos el objeto herramienta que ya teniamos creada con el molde
                       
            
        case 2:
            miTaller.mostrar_todas_las_herramientas()
            
        case 3:
            #En este caso hay que tomar en cuenta los parametros que tiene el metodo, que son codigo, cliente, dias
            codigo = int(input("Ingrese el codigo de la herramienta: "))
            cliente = input("Ingrese el nombre del cliente: ")
            dias = int(input("Ingrese los dias que se tomara la herramienta: "))
            
            renta = miTaller.rentar_herramienta(codigo, cliente, dias)
            #El valor que recibe renta es True or False
            
            if renta: #Aqui es lo mismo que decir renta == True
                herramienta = miTaller.buscar_herramienta(codigo)
                total = herramienta.calcular_total() #Devolvemos el valor total en total
            
            
        case 4:
            codigo = int(input("Ingrese el codigo de la herramienta: "))
            pago = int(input("Ingrese el pago de la herramienta: "))
            
            devuelta = miTaller.devolver_herramienta(codigo, pago)
            herra = miTaller.buscar_herramienta(codigo)
            encontrada = herra.calcular_total()
            
            print(f"El total que se tiene que devolver es de {encontrada}")
            if devuelta is not False:
                print(f"El total es de {devuelta}")
        case 5:
            miTaller.herramientas_disponibles()
            
        case 6:
            miTaller.herramientas_rentadas
            
        case 7:
            miTaller.resumen_taller()
        
        case 8: 
            break
        
        
    
        
    
    
        