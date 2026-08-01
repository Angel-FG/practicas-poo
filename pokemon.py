import random

class Pokemon():
    def __init__(self, nombre, nivel, fuerza, defensa, velocidad, hp_maximo):
        self.nombre = nombre
        self.nivel = nivel
        self.fuerza = fuerza
        self.defensa = defensa
        self.velocidad = velocidad
        self.hp_maximo = hp_maximo
        
        #vida que va a subir y bajar en batallas
        self._hp_actual = hp_maximo
    
    @property
    def hp(self):
        return self._hp_actual
    
    @hp.setter
    def hp(self, nueva_vida):
        if nueva_vida < 0:
            self._hp_actual = 0
        else:
            self._hp_actual = nueva_vida
        
    def vivo(self):
        if self.hp > 0:
            return True
        return False
        
    def muerto(self):
        if self.hp== 0:
            print(f"El pokemon {self.nombre} esta debilitado")
    
    def atacar(self, enemigo):
        daño = self.fuerza - enemigo.defensa
        if daño <= 0:
            daño = 1
        enemigo.hp = enemigo.hp - daño
        enemigo.muerto()
        
    def curar(self, cantidad):
        self.hp = self.hp + cantidad
        
        if self.hp > self._hp_actual:
            self.hp = self.hp_maximo
    
    def __str__(self):
        return f"El pokemon {self.nombre} de nivel {self.nivel} tiene {self.hp} de vida"
        
class Entrenador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []
        self.mochila = {
            "pociones": 3,
            "Pokebolas": 5
            }
     
    #Necesita recibir el objeto (nuevo_pokemon)   
    def captura(self, nuevo_pokemon):
        if self.mochila["Pokebolas"] > 0 and len(self.equipo) < 6:
            print(f"El entrenador {self.nombre} ha lanzado una pokebola")
            self.mochila["Pokebolas"] -= 1 
            
            self.equipo.append(nuevo_pokemon)
            print(f"Has atrapado a un nuevo pokemon {nuevo_pokemon.nombre}")
        elif len(self.equipo) > 6:
            print("Tu equipo esta completo")
        else:
            print("No tienes suficientes pokebolas")
               
    def mostrar_equipo(self):
        if len(self.equipo) == 0:
            print("No hay pokemones")
        else:
            for pokemon in self.equipo:
                print(pokemon)
    
    def usar_pociones(self):
        if self.mochila["pociones"] > 0 and len(self.equipo) > 0:
            self.mochila["pociones"] -= 1 
            self.equipo[0].curar(20)
            print("Has usado una pocion")
        else:
            print("No tienes pociones o tu equipo no tiene pokemones")
            
            
def generar_pokemon_aleatorio(nivel_min, nivel_max):
    nombre = ["pidgey", "onix", "machomp", "abra", "geodude"]
    nombre_elegido = random.choice(nombre)
    nivel_elegido = random.randint(nivel_min, nivel_max)
        
    fuerza = 4 * nivel_elegido
    defensa = 2 * nivel_elegido
    velocidad = random.randint(5,15) * nivel_elegido
    hp = 15 * nivel_elegido
        
    return Pokemon(nombre_elegido, nivel_elegido, fuerza, defensa, velocidad, hp)
    
    
mi_personaje = Entrenador("Angel")

while True:
    print("\t Bienvenido al sistema de captura pokemon")
    print("1) Explorar la hierba alta")
    print("2) Retar al rival")
    print("3) Ver al equipo")
    print("4) Usar pociones")
    print("5) Salir")
    
    try:
        opcion = int(input("Que opcion desea elegir: "))
    except ValueError:
        print("Ingrese solo numeros")
        continue
    
    match opcion:
        case 1:
            salvaje = generar_pokemon_aleatorio(2,10)
            print(f"Ha aparecido un pokemon salvaje es un {salvaje.nombre} de nivel {salvaje.nivel}")
            mi_personaje.captura(salvaje)
        case 2:
            if len(mi_personaje.equipo) == 0:
                print("No tienes pokemones para pelear")
                continue
            
            rival = Entrenador("Oscar")
            
            for _ in range(3):
                rival.equipo.append(generar_pokemon_aleatorio(3,12))
                
            print(f"El rival {rival.nombre} te ha desafiado")
            
            mi_luchador = mi_personaje.equipo[0]
            su_luchador = rival.equipo[0]
            
            print(f"Ve {mi_luchador.nombre}")
            print(f"{rival.nombre} ha enviado a {su_luchador.nombre}")
            
            while mi_luchador.vivo() and su_luchador.vivo():
                input("Presiona Enter para el siguiente turno")
                
                if mi_luchador.velocidad >= su_luchador.velocidad:
                    primero = mi_luchador
                    segundo = su_luchador
                else:
                    primero = su_luchador
                    segundo = mi_luchador
                    
                primero.atacar(segundo)
                
                if segundo.vivo():
                    segundo.atacar(primero)
                    
                if mi_luchador.vivo():
                    print(f"Ganaste {su_luchador.nombre} ha muerto")
                else:
                    print(f"Perdiste tu {mi_luchador.nombre} ha muerto")
            
        case 3:
            mi_personaje.mostrar_equipo()
            
        case 4:
            mi_personaje.usar_pociones()
            
        case 5:
            break
        
        case _:
            print("opcion invalida")