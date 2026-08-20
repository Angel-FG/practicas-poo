class Empleado:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        
    def trabajar(self):
        print("Estoy trabajando")
        
class Programador(Empleado):
    def __init__(self, codigo, nombre, lenguaje):
        super().__init__(codigo, nombre)
        self.lenguaje = lenguaje
        
    def trabajar(self):
        super().trabajar()
        print("Estoy programando")
        
    def __str__(self):
        return f"Codigo: {self.codigo} : Nombre: {self.nombre} : Lenguaje: {self.lenguaje}"

class Diseñador(Empleado):
    def __init__(self, codigo, nombre, herramientaDiseño):
        super().__init__(codigo, nombre)
        self.herramientaDiseño = herramientaDiseño
        
    def trabajar(self):
        super().trabajar()
        print("Estoy diseñando")
        
    def __str__(self):
        return f"Codigo: {self.codigo} : Nombre: {self.nombre} : Herramienta de Diseño: {self.herramientaDiseño}"
    
class DesarrolladorUI(Programador, Diseñador):
    def __init__(self, codigo, nombre, lenguaje, herramientaDiseño, desarrollo):
        Programador().__init__(codigo, nombre, lenguaje)
        Diseñador().__init__(codigo, nombre, herramientaDiseño)
        self.desarrollo = desarrollo
    
    #Para poder hacer que especificamente un metodo de alguna de las dos clases padres funcione lo que tenemso que hacer es especificar como quiere trabajar en un metodo especifico
    def trabajar(self):
        super().trabajar()
        print("Estoy Trabajando muy bien")
        
    def trabajandoProgramador(self):
        Programador.trabajar()
        
    def trabajandoDiseñador(self):
        Diseñador.trabajar()
        
    def __str__(self):
        return f"Nombre: {self.nombre} : Lenguaje: {self.lenguaje} : Herramienta de Diseño: {self.herramientaDiseño} : Desarrollo: {self.desarrollo}"
        
class Empresa:
    def __init__(self):
        self.registrarEmpleados = {}
        
    def registrarEmpleado(self, empleado):
        if empleado in self.registrarEmpleados:
            print("El empleado ya existe")
            return False
        
        self.registrarEmpleados[empleado.codigo] = empleado
        return True
    
    def buscarEmpleado(self, codigo):
        return self.registrarEmpleados.get(codigo)
    
    def mostrarDatos(self, codigo):
        buscar = self.buscarEmpleado(codigo)
        
        if buscar is None:
            print("El empleado no existe")
            return False
        
        print(buscar)
        return True
    
    def ejecutarComoProgramador(self, codigo):
        empleado = self.buscarEmpleado(codigo)
        
        if empleado is None:
            print("El empleado no existe")
            return False
        
        if isinstance(empleado, DesarrolladorUI):
           empleado.trabajandoProgramador()
        elif isinstance(empleado, Programador):
            empleado.trabajar()
        else:
            print(f"Error: empleado {empleado.nombre} no es un programadro")
        return True
    
    def ejecutarComoDiseñador(self, codigo):
        empleado = self.buscarEmpleado(codigo)
                
        if empleado is None:
            print("El empleado no existe")
            return False
        
        if isinstance(empleado, DesarrolladorUI):
            empleado.trabajandoDiseñador()
        elif isinstance(empleado, Diseñador):
            empleado.trabajar()
        else:
            print(f"Error: {empleado.nombre} no sabe diseñar")
        return True
    
    def ejecutarComoAmbos(self, codigo):
        empleado = self.buscarEmpleado(codigo)
                        
        if empleado is None:
            print("El empleado no existe")
            return False
        
        if isinstance(empleado, DesarrolladorUI):
            empleado.trabajar()
        else:
            print("El empleado no sabe que hacer")
        return True
    
    def crearProgramador(self):
        codigo = leerEntero("Ingrese el codigo: ")
        nombre = leerTexto("Ingrese el nombre: ")
        lenguaje = leerTexto("Ingrese el lenguaje: ")
        
        programador = Programador(codigo, nombre, lenguaje)
        self.registrarEmpleado(programador)
        
    def crearDiseñador(self):
        codigo = leerEntero("Ingrese el codigo: ")
        nombre = leerTexto("Ingrese el nombre: ")
        herramientaDiseño = leerTexto("Ingrese la herramienta: ")
        
        diseñador = Diseñador(codigo, nombre, herramientaDiseño)
        self.registrarEmpleado(diseñador)
        
    def diseñadorUI(self):
        codigo = leerEntero("Ingrese el codigo: ")
        nombre = leerTexto("Ingrese el nombre: ")
        lenguaje = leerTexto("Ingrese el lenguaje: ")
        herramientaDiseño = leerTexto("Ingrese la herramienta: ")
        desarrollo = leerTexto("Ingrese desarrollo: ")
        
        desarrolladorUI = DesarrolladorUI(codigo, nombre, lenguaje, herramientaDiseño, desarrollo)
        self.registrarEmpleado(desarrolladorUI)
        
    
def leerEntero(mensaje):
    while True:
        try:
            entero = int(input(mensaje))
        except:
            print("Solo numeros enteros")
        return entero
    
def leerTexto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("El valor no puede estar vacio")


def menu():
    miEmpresa = Empresa()
    while True:
        print("=" * 100)
        print("1) Crear empleados")
        print("2) Mostrar sus datos")
        print("3) Ejecutar comportamiento programador")
        print("4) Ejecutar comportamiento diseñador")
        print("5) Ejecutar ambos comportamientos")
        print("6) Salir")
        
        opcion = leerEntero("Ingrese un valor: ")
        
        match opcion:
            case 1:
                print("Seleccione el tipo de empleado")
                print("1) Programador")
                print("2) Diseñador")
                print("3) Desarrollador UI")
                tipo = leerEntero("Que empleado desea registrar?")
                
                match tipo:
                    case 1:
                        miEmpresa.crearProgramador()
                    case 2:
                        miEmpresa.crearDiseñador()
                    case 3:
                        miEmpresa.diseñadorUI()
                    case _:
                        print("Opcion invalida")
            case 2:
                codigo = leerEntero("Ingrese el codigo del empleado que quiere ver: ")
                miEmpresa.mostrarDatos(codigo)
            case 3:
                codigo = leerEntero("Ingrese el codigo del empleado: ")
                miEmpresa.ejecutarComoDiseñador(codigo)
            case 4:
                codigo = leerEntero("Ingrese el codigo del empleado: ")
                miEmpresa.ejecutarComoProgramador(codigo)
            case 5:
                codigo = leerEntero("Ingresa el codigo del empleado solo UI: ")
                miEmpresa.ejecutarComoAmbos(codigo)
            case 6:
                break
            case _:
                print("Ingrese un numero valido")           

if __name__=="__main__":
    menu()