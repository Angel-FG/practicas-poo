portafolio = []

while True:
    print("Propiedades")
    print("1) Comprar propiedad")
    print("2) Ver portafolio")
    print("3) Calcular ingresos mensuales")
    print("4) Rentar propiedad")

    try:
        opcion = int(input("Seleccione una opcion: "))
        
    except ValueError:
        print("Tiene que ser un numero")
        continue
        
    match opcion:
        case 1:
            nombre = input("Ingrese el nombre de la propiedad: ")
            renta = float(input("Ingrese la renta mensual de la propiedad: "))
            
            diccionario = {
                "nombre": nombre,
                "renta": renta,
                "rentada": False
            }
            
            portafolio.append(diccionario)
            
            print("Felicidades has obtenido una nueva propiedad")
            
        case 2:
            #Visualizacion de los datos mas ejemplares
            if len(portafolio) == 0:
                print("Aun no tienes propiedades")
                
            for propiedad in portafolio:
                #Extraemos los datos para que el codigo se mas sencillo de leer
                nombre_depa = propiedad["nombre"]
                precio = propiedad["renta"]
                
                if propiedad["rentada"] == True:
                    print(f"{nombre_depa} tiene una renta de {precio} y su estado: [Ocupada]")
                else:
                    print(f"{nombre_depa} tiene una renta de {precio} y su estado: [Disponible]")
        case 3:
            total = 0
            
            for propiedad in portafolio:
                if propiedad["rentada"] == False:
                    print("Esta propiedad no esta siendo rentada")
                else:
                    total += propiedad["renta"]
            print(f"El total de sus ingresos son {total}")
                
        case 4:
            rentar_propiedad = input("Ingrese el nombre de la propiedad que desea rentar: ")
            encontrado = False
            for propiedad in portafolio:
                if propiedad["nombre"].lower() == rentar_propiedad.lower():
                    encontrado = True
                    propiedad["rentada"] = True
                    print("Se he esta rentando esa propiedad")
                    
            if not encontrado:
                print("Esa propiedad no existe")
                
        
        case 5:
            break 
        
        