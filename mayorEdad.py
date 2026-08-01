class Mayor:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mayor_Edad(self):
        if self.edad < 18:
            print(f"{self.nombre} tiene menos de 18 tiene {self.edad}")
        else:
            print(f"{self.nombre} es mayor de edad tiene {self.edad}")
            
    #def __str__(self):
     #   return f"La persona {self.nombre} se registro con una edad de {self.edad}"
            
Chico1 = Mayor("Angel", 17)

Chico1.mayor_Edad()

