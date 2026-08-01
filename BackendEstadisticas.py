class Jugador():
    def __init__(self, nombre, bajas, muertes):
        self.nombre = nombre
        self.bajas = bajas
        self.muertes = muertes
        
    def calcular_kd(self):
        if self.muertes == 0:
            print("No se puede dividir entre cero")
        else:
            kd = self.bajas/self.muertes
            print(kd)
            
    def __str__(self):
        return f"EL jugador {self.nombre} tiene {self.bajas} kills y ha muerto {self.muertes}"

class Escuadron():
    def __init__(self, nombre_escuadron):
        self.nombre_escuadron = nombre_escuadron
        self.jugadores = []
        
    def reclutar(self, jugador):
        
        if not isinstance(jugador, Jugador):
            raise TypeError("Solo se pueden reclutar jugadores")
        
        if len(self.jugadores) < 4:
            self.jugadores.append(jugador)
            print(f"{jugador.nombre} ha sido reclutado")
        else:
            print(f"No se puede reclutar al jugador porque ya esta lleno el escuadron")
        
    def mostrar_estadisticas(self):
        for jugador in self.jugadores:
            print(jugador)
            
    def buscar_mvp(self):
        # Si la lista esta vacia no se puede buscar a nadie
        if len(self.jugadores) == 0:
            print("No hay jugadores para mostrar")
            return
        
        mvp_temporal = self.jugadores[0]
        
        # Va a recorrer la lista uno por uno
        for jugador in self.jugadores:
            if jugador.bajas > mvp_temporal.bajas:
                mvp_temporal = jugador
        print(f"El mvp es {mvp_temporal.nombre} con {mvp_temporal.bajas}")
        
nuevo_escuadron = Escuadron("Tilines")

while True:
    print("1) Reclutar jugador")
    print("2) Ver estado del escuadron")
    print("3) Mostrar al MVP de la partida")
    print("4) Salir")
    
    try:
        opcion = int(input("Seleccione una opcion: "))  
    except ValueError:
        print("Solo ingrese numero")
        continue
    
    match opcion:
        case 1:
            nombre = input("Ingrese su nombre: ")
            kills = int(input("Ingrese sus kills: "))
            muertes = int(input("Ingrese sus muertes: "))
            
            nuevo_jugador = Jugador(nombre, kills, muertes)
            nuevo_escuadron.reclutar(nuevo_jugador)
            pass
        case 2:
            nuevo_escuadron.mostrar_estadisticas()
        case 3:
            nuevo_escuadron.buscar_mvp()
        case 4:
            break