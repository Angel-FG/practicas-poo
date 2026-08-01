mochila = []


while True:
    print("1) Recoger objeto")
    print("2) Ver inventario")
    print("3) Buscar objeto")
    print("4) Salie")
    
    try:
        opcion = int(input("Elige una de las opciones: "))
    except ValueError:
        print("Deben de ser solo numero validos")
        continue
    
    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del objeto: ")
            cantidad = int(input("Ingrese cuaantos objetos recogio: "))
            rareza = input("Ingrese la rareza del objeto: ")
            
            loot = {
                "nombre": nombre,
                "cantidad": cantidad,
                "rareza": rareza
            }
            
            mochila.append(loot)
            
            print("Se ha guardado correctamente el loot")
        case 2:
            if len(mochila) == 0:
                print("No tiene objetos para mostrar")
                
            for objetos in mochila:
                nombre_objeto = objetos["nombre"]
                cantidad_objeto = objetos["cantidad"]
                rareza_objeto = objetos["rareza"]
                
                print(f"El jugador recogio {cantidad_objeto} {nombre_objeto} con rareza {rareza_objeto}")
                    
        case 3:
            recogido = input("Que objeto desea buscar: ")
            encontrado = False
            
            for objetos in mochila:
                if objetos["nombre"].lower() == recogido.lower():
                    encontrado = True
                    print(f"El jugador tiene ese objeto y tiene {objetos['cantidad']} de {objetos['nombre']}")
            if not encontrado:
                print("El objeto no fue encontrado")
        case 4:
            break
     
     
    