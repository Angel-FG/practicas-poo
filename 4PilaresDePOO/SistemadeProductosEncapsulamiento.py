class Product:
    def __init__(self, codigo, nombre, categoria):
        self.__codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = 0
        self.__stock = 0
        self._estado = "Disponible"
    
    @property 
    def codigo(self):
        #Funcion de solo lectura
        return self.__codigo
    
    @property
    def estado(self):
        return self._estado
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevoPrecio):
        if not isinstance(nuevoPrecio, int):
            print("El valor debe de ser solo numeros")
            return False
        
        if nuevoPrecio <= 0:
            print("El precio no puede ser menor a 0 o igual a cero")
            return False
        
        self.__precio = nuevoPrecio
        return True
        
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, nuevoStock):
        if not isinstance(nuevoStock, int):
            print("Solo se permiten valores enteros")
            return False
        
        if nuevoStock < 0:
            print("El stock no puede ser negativo")
            return False
        
        if self.__stock > 0: # 20 + 10 = 30
            self.__stock += nuevoStock
            print(f"Se han puesto mas productos la nueva cantidad de productos es {self.__stock}")
        else:
            self.__stock = nuevoStock # 20
            print(f"Se ingresaron productos el nuevo stock es de {nuevoStock}")
            
        return True
    
    def venta(self, cantidad):
        if not isinstance(cantidad, int):
            print("Solo se aceptan valores numericos")
            return False
        
        if self.__stock == 0:
            self._estado = "Agotado"
            print("El stock se ha agotado")
            return False
        
        if self._estado == "Agotado":
            print("El producto esta sin existencias")
            return False
        
        self.__stock -= cantidad
        print(f"Se ha vendido {cantidad} {self.nombre} el nuevo stock de {self.nombre} es de {self.__stock}")
        return True
            
    def __str__(self):
        return f"Codigo: {self.__codigo} | Nombre: {self.nombre} | Categoria: {self.categoria}"
    
class Store:
    def __init__(self):
        self.producto = {}
        self.borrador = {}
        
    def crearBorrador(self, producto):
        if producto.codigo in self.borrador:
            print("El codigo ya existe dentro del borrador")
            return False
        
        self.borrador[producto.codigo] = producto
        return True
    
    def mostrarBorradores(self):
        if len(self.borrador) == 0:
            print("No existe ningun producto dentro de borradores")
            return False
        
        for producto in self.borrador.values():
            print(producto)
        return True    

    def registrarProducto(self, codigo):
        #Las llaves del diccionario son los codigos cuidado con esto
        #1. Verificamos que el codigo exista en la sala de espera
        if codigo not in self.borrador:
            print("El producto no existe")
            return False
        
        #2. Sacamos el objeto del diccionario borrador
        objetoCompleto = self.borrador[codigo]
        
        #3. Checamos si el producto ya se encuentra registrado
        if codigo in self.producto:
            print("El codigo ya esta registrado")
            return False
        
        #4. Lo registramos en la tienda
        self.producto[codigo] = objetoCompleto

        #5. Lo borramos de borradores
        del(self.borrador[codigo])
        print(f"Se ha registrado correctamente {objetoCompleto.nombre}")
        return True
    
    def buscarProducto(self, codigo):
        return self.producto.get(codigo)
    
    def mostrarTodosLosProductos(self):
        for productos in self.producto.values(): #Se me olvidaron los ()
            print(productos)
            
    def eliminarProducto(self, codigo):
        productoEliminar = self.buscarProducto(codigo)
        
        if productoEliminar is None:
            print("El producto no existe")
            return False
        
        del(self.producto[productoEliminar.codigo]) #No puedo pasarle el objeto completo para borrar, debo o pasarle el atributo codigo en el objeto o solo pasar codigo
        print("El producto se ha eliminado correctamente")   
        return True
    
    def venderProducto(self, codigo, cantidad):
        productoVender = self.buscarProducto(codigo)
        
        if productoVender is None:
            print("El producto no existe")
            return False
        
        productoVender.venta(cantidad)
        return True
        
    def reponerExistencias(self, codigo, cantidad):
        productoReponer = self.buscarProducto(codigo)
        
        if productoReponer is None:
            print("El producto no existe")
            return False
        
        #Recordar que al momento de usar encapsulamiento los metodos se llaman sin () solamente como si declararas una variable
        productoReponer.stock = cantidad
        return True
    
    def cambiarPrecio(self, codigo, nuevoPrecio):
        objetoNuevoPrecio = self.buscarProducto(codigo)
        
        if objetoNuevoPrecio is None:
            print("El producto no existe")
            return False
        
        #Aqui tambien misma falla
        objetoNuevoPrecio.precio = nuevoPrecio
        return True
        
    def productoDisponibles(self):
        for producto in self.producto.values():
            if producto.estado == "Disponible":
                print(producto)
                
    def productoAgotado(self):
        for producto in self.producto.values():
            if producto.estado == "Agotado":
                print(producto)
    
        
def leerEntero(entero):
    while True:
        try:
            return int(input(entero))
        except ValueError:
            print("El valor debe de ser un valor entero")
        
def leerTexto(texto):
    while True:
        mensaje = input(texto).strip()
        if mensaje:
            return mensaje
        print("El mensaje no puede estar vacio")
        
def menu():
    
    miTienda = Store()
    
    espera = {}

    while True:
        print(100*("="))
        print("Sistema Productos")
        print("1) Crear Producto")
        print("2) Registrar Producto")
        print("3) Mostrar todos los productos")
        print("4) Eliminar un producto")
        print("5) Vender producto")
        print("6) Reponer existencas de un producto")
        print("7) Cambiar precio de un producto")
        print("8) Productos disponibles")
        print("9) Productos agotads")
        print("10) Salir")
        
        opcion = leerEntero("Seleccione una opcion: ")
        
        match opcion:
            case 1:
                codigo = leerEntero("Ingrese el codigo del producto: ")
                nombre = leerTexto("Ingrese el nombre del producto: ")
                categoria = leerTexto("Ingrese la categoria del producto: ")
                
                miProducto = Product(codigo, nombre, categoria)
                print("Se ha creado correctamente el producto")
                miTienda.crearBorrador(miProducto)
            case 2:
                hayBorradores = miTienda.mostrarBorradores()
                
                if hayBorradores:
                    codigo = leerEntero("Ingrese el codigo del producto que va a registrar: ")
                    
                    miTienda.registrarProducto(codigo)
            case 3:
                miTienda.mostrarTodosLosProductos()
            case 4:
                codigo = leerEntero("Ingrese el codigo del producto que desea eliminar: ")
                miTienda.eliminarProducto(codigo)
            case 5:
                codigo = leerEntero("Ingrese el codigo del producto que se va a vender: ")
                cantidad = leerEntero("Ingrese la cantidad de productos que se van a vender: ")
                miTienda.venderProducto(codigo, cantidad)
            case 6:
                codigo = leerEntero("Ingrese el codigo del producto que se va a reponer: ")
                cantidad = leerEntero("Ingrese la cantidad de productos que se van a reponer: ")
                miTienda.reponerExistencias(codigo, cantidad)
            case 7:
                codigo = leerEntero("Ingrese el codigo del producto que va a cambiar el precio: ")
                precio = leerEntero("Ingrese el nuevo precio del producto: ")
                miTienda(codigo, precio)
            case 8:
                miTienda.productoDisponibles()
            case 9:
                miTienda.productoAgotado()
            case 10:
                break
            case _:
                print("Opcion invalida seleccione del 1 al 10")
                
if __name__=="__main__":
    menu()
