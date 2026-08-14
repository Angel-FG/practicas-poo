class Persona:
    def __init__(self, edad, altura):
        self.edad = edad
        self.altura = altura
        
    def saltar(self):
        print(f"La persona puede saltar con {self.edad}")
        
class Padre(Persona):
    def __init__(self, edad, altura, nombre):
        super().__init__(edad, altura)
        self.nombre = nombre

class Niño(Persona, Padre):
    def __init__(self, edad, altura, nombre):
        Persona().__init__(edad, altura)
        Padre().__init__(edad, altura, nombre)
        self.nombre = nombre
        
    def saltar(self):
        print(f"El niño con {self.edad} no puede saltar")
        
    def salto(self):
        return f'{super.saltar()}'
        
jose = Niño(8, 1.87, "Jose")
jose.salto()