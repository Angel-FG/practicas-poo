
"""
El Spawn (__init__):
Debe recibir dos datos obligatorios cuando nazca el alumno: nombre y matricula. Además, debe inicializar automáticamente una variable 
llamada self.calificaciones con una lista vacía ([]).

El Traductor (__str__): Crea el método especial para que, si alguien imprime al alumno con un print(), devuelva un texto bonito con su nombre 
y matrícula.

El Botón de Calificaciones: Crea un método llamado agregar_calificacion(self, nota) que agarre esa nota y la meta a la lista de calificaciones
usando .append(nota).
"""

class Alumno():
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = []
        
    def __str__(self):
        return f"El alumno se llama {self.nombre} y tiene de matricula {self.matricula}"
        
    def agregar_calificaciones(self, notas):
        self.calificaciones.append(notas)
        print(f"El alumno {self.nombre} tiene de calificacion {self.calificaciones}")

alumno1 = Alumno("Angel", 23380669)

alumno1.agregar_calificaciones(80)
alumno1.agregar_calificaciones(90)    

print(alumno1)    