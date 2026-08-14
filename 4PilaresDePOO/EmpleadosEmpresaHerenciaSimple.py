class Employee:
    def __init__(self, nombre, noDeEmpleado, salario, añosTrabajando):
        self.nombre = nombre
        self.noDeEmpleado = noDeEmpleado
        self.salario = salario
        self.añosTrabajando = añosTrabajando
        
    def trabajando(self):
        print("Estoy trabajando")    
    
class Programador(Employee):
    def __init__(self, nombre, noDeEmpleado, salario, añosTrabajando, lenguaje, nivel):
        super().__init__(nombre, noDeEmpleado, salario, añosTrabajando)
        self.lenguaje = lenguaje
        self.nivel = nivel
        
    def trabajando(self):
        super().trabajando()
        print("Estoy programando")
        
    def __str__(self):
        return f"Nombre: {self.nombre} | Numero de Empleado: {self.noDeEmpleado} | Salario: {self.salario} | Años Trabajando: {self.añosTrabajando} | Lenguaje: {self.lenguaje} | Nivel: {self.nivel}"
        
class Diseñador(Employee):
    def __init__(self, nombre, noDeEmpleado, salario, añosTrabajando, herramientaPrincipal, AreaDiseño):
        super().__init__(nombre, noDeEmpleado, salario, añosTrabajando)
        self.herramientaPrincipal = herramientaPrincipal
        self.AreaDiseño = AreaDiseño
        
    def trabajando(self):
        super().trabajando()
        print("Estoy diseñando")
        
    def __str__(self):
        return f"Nombre: {self.nombre} | Numero de Empleado: {self.noDeEmpleado} | Salario: {self.salario} | Años Trabajando: {self.añosTrabajando} | Herramienta Principal: {self.herramientaPrincipal} | Area de diseño: {self.AreaDiseño}"

class Empresa:
    def __init__(self):
        self.guardar = {}
        
    def registrarTrabajador(self, codigo):
        if codigo.noDeEmpleado in self.guardar:
            print("El empleado ya esta registrado")
            return False
        
        self.guardar[codigo.noDeEmpleado] = codigo
        print("Se ha registrado el usuario")
        return True
    
    def buscarEmpleado(self, noEmpleado):
        return self.guardar.get(noEmpleado)
    
    def mostrarEmpleado(self, codigo):
        buscar = self.buscarEmpleado(codigo)
        
        if buscar is None:
            print("El empleado no existe")
            return False
        
        print(buscar)
        return True
    
    def ponerseaTrabajar(self, codigo):
        empleado = self.buscarEmpleado(codigo)
        
        if empleado is None:
            return False
        
        empleado.trabajando()
        return True
        
def leerEntero(entero):
    while True:
        try:
            return int(input(entero))
        except ValueError:
            print("El valor debe de ser un numero entero")
            
def leerTexto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("El valor no puede estar vacio")
        
def Ejecutarmenu():
    miEmpresa = Empresa()
    while True:
        print(100*"==")
        print("1) Crear Programador")
        print("2) Crear Diseñador")
        print("3) Mostrar informacion de un empleado")
        print("4) Hacer trabajar a un empleado")
        print("5) Salir")
        
        opcion = leerEntero("Ingrese un numero del 1 al 5: ")
        
        match opcion:
            case 1:
                nombre = leerTexto("Ingrese el nombre del empleado: ")
                noEmpleado = leerEntero("Ingrese el numero unico del empleado: ")
                salario = leerEntero("Ingrese el salario del empleado: ")
                añosTrabajando = leerEntero("Ingrese la cantidad de años que esta trabajando el usuario: ")
                lenguaje = leerTexto("Ingrese el lenguaje del programador: ")
                nivel = leerTexto("Ingrese el nivel del programador: ")
                programador = Programador(nombre, noEmpleado, salario, añosTrabajando, lenguaje, nivel)
                miEmpresa.registrarTrabajador(programador)
            case 2:
                nombre = leerTexto("Ingrese el nombre del empleado: ")
                noEmpleado = leerEntero("Ingrese el numero unico del empleado: ")
                salario = leerEntero("Ingrese el salario del empleado: ")
                añosTrabajando = leerEntero("Ingrese la cantidad de años que esta trabajando el usuario: ")
                herramientaPrincipal = leerTexto("Ingrese la herramienta del diseñador/a: ")
                areaDeTrabajo = leerTexto("Ingrese el area de trabajo del deiseñador/a: ")
                programador = Diseñador(nombre, noEmpleado, salario, añosTrabajando, herramientaPrincipal, areaDeTrabajo)
                miEmpresa.registrarTrabajador(programador)
            case 3:
                codigo = leerEntero("Ingrese el codigo del empleado que quiere ver: ")
                miEmpresa.mostrarEmpleado(codigo)
            case 4:
                codigo = leerEntero("Ingrese el codigo del empleado que quiera poner a trabajar: ")
                miEmpresa.ponerseaTrabajar(codigo)
            case 5:
                break
            case _:
                ("Ingrese un valor valido")
    
    
if __name__ == "__main__":
    Ejecutarmenu()
    