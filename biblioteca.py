class Libro():
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.estado = "Disponible"
    
    def prestar(self):
        if self.estado == "Prestado":
            print("El libro ya esta prestado")
            return False
        
        self.estado = "Prestado"
        print("El libro fue prestado correctamente")
        return True

    def devolver(self):
        if self.estado == "Prestado":
            self.estado = "Disponible"
            print("El libro ha sido devuelto correctamente")
            return True
        
        else:
            print("El libro no estaba prestado")
            return False
        
        
    def __str__(self):
        return f"Codigo {self.codigo} | Libro: {self.titulo} | Autor: {self.autor} | Estado: {self.estado}"


class Biblioteca():
    def __init__(self):
        #type hinting
        self.objetos: list[Libro] = []
        
    def agregar_libro(self, libro):
        for libro_guardado in self.objetos:
            if libro_guardado.codigo == libro.codigo:
                print("El libro ya se encuentra en la biblioteca")
                return False
            
        self.objetos.append(libro)
        return True
    
    def mostrar_libros(self):
        for libros in self.objetos:
            print(libros)

    def buscar_libro(self, codigo):
        for buscar_libro in self.objetos:
            if buscar_libro.codigo == codigo:
                return buscar_libro
        
        return None
        
    def mostrar_disponibles(self):
        if len(self.objetos) == 0:
            print("No hay libros registrados. Registre un libro")
            return None
        
        hay_disponibles = False
        
        for libros in self.objetos:
            if libros.estado == "Disponible":
                print(libros)
                hay_disponibles = True
         
        if not hay_disponibles:   
            print("No hay libros disponibles")
            return False
        
        return True
    
mi_biblioteca = Biblioteca()
    
while True:
    print("1. Registrar libro")
    print("2. Mostrar todos los libros")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar libros disponibles")
    print("6. Salir")
    
    try:
        opcion = int(input("Ingrese una de las opciones disponibles: \n"))
    except ValueError:
        print("Ingrese un numero")
        continue

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del libro: ")
            autor = input("Ingrese el nombre del autor: ")
            codigo = input("Ingrese el codigo del libro: ")
            
            libro = Libro(nombre, autor, codigo)
            
            print(f"Titulo: {nombre} \n Autor: {autor} \n Codigo: {codigo}")
            
            mi_biblioteca.agregar_libro(libro)
        case 2:
            mi_biblioteca.mostrar_libros()
        case 3:
            codigo = input("Ingrese el codigo del libro: ")
            libro_encontrado = mi_biblioteca.buscar_libro(codigo)
            if libro_encontrado is not None:
                libro_encontrado.prestar()
            else:
                print("Ese libro no existe")
        case 4:
            codigo = input("Ingrese el codigo del libro: ")
            libro_encontrado = mi_biblioteca.buscar_libro(codigo)
            if libro_encontrado is not None:
                libro_encontrado.devolver()
            else:
                print("No se ha encontrado el libro")
        case 5:
            mi_biblioteca.mostrar_disponibles()
        case 6:
            break
        
            