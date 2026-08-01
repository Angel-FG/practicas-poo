class Mascota:
    def __init__(self, nombre, especie, codigo):
        self.nombre = nombre
        self.especie = especie
        self.codigo = codigo
        self.estado = "Disponible"
        
    def adoptar(self):
        if self.estado == "Adoptada":
            print("La mascota ya ha sido adoptada")
            return False
        
        self.estado = "Adoptada"
        print("La mascota fue adoptada")
        return True
    
    def regresar(self):
        if self.estado == "Adoptada":
            self.estado = "Disponible"
            return True
        
        #self.estado == "Disponible" Esta linea sobra ya que no la uso en nada
        print("La mascota esta disponible")
        return False
    
    def __str__(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Especie: {self.especie} | Estado: {self.estado}"
    
class Refugio:
    def __init__(self):
        self.objeto = []
        
    def agregar_mascota(self, mascota):
        for mascota_guardada in self.objeto:
            if mascota_guardada.codigo == mascota.codigo:
                print("La mascota ya esta registrada")
                return False
        
        self.objeto.append(mascota)
        print("Se ha guardado la mascota correctamente")
        return True
    
    def buscar_mascota(self, codigo):
        if len(self.objeto) == 0:
            return None
        
        for mascota_encotrada in self.objeto:
            if mascota_encotrada.codigo == codigo:
                return mascota_encotrada
        
        return None
    
    def mostrar_mascotas(self):
        if len(self.objeto) == 0:
            print("No hay mascotas disponibles")
            return None
        
        for mascotas in self.objeto:
            print(mascotas)
            
    def mostrar_disponibles(self):
        hay_mascotas = False
        
        for mascotas in self.objeto:
            if mascotas.estado == "Disponible":
                print(mascotas)
                hay_mascotas = True
                
        if not hay_mascotas:
            print("No hay mascotas disponibles")
            return False
        
        return True
    
mi_refugio = Refugio()
    
while True:
    print("\t Refugio de mascotas")
    print("1) Registrar mascotas")
    print("2) Mostrar todas las mascotas")
    print("3) Adoptar mascota")
    print("4) Regresar mascota")
    print("5) Mostrar mascotas disponibles")
    print("6) Salir")
    
    try:
        opcion = int(input("Ingrese una opcion disponible: "))
    except ValueError:
        print("Solo opciones disponibles numericas")
        continue
        
    if opcion < 1 or opcion > 6:
        print("Solo opciones del 1 al 6")
        continue
    
    match opcion:
        case 1:
            nombre = input("Ingrese el nombre de la mascota: ")
            especie = input("Ingrese el nombre de la especie: ")
            codigo = input("Ingrese el codigo de la mascota: ")
            
            mascota = Mascota(nombre, especie, codigo)
            
            mi_refugio.agregar_mascota(mascota)
        case 2:
            mi_refugio.mostrar_mascotas()
        case 3:
            codigo = input("Ingrese el codigo de la mascota: ")
            mi_mascota = mi_refugio.buscar_mascota(codigo)
            
            if mi_mascota is not None:
                mi_mascota.adoptar()
            else:
                print("No existe esa mascota")
        case 4:
            codigo = input("Ingrese el codigo de la mascota: ")
            mi_mascota = mi_refugio.buscar_mascota(codigo)
            
            if mi_mascota is not None:
                mi_mascota.regresar()
            else:
                print("No existe esa mascota")
            
        case 5:
            
            mi_refugio.mostrar_disponibles()
            
        case 6:
            break