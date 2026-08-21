def punteros(arreglo):
    izquierdo = 0
    derecho = len(arreglo) - 1
    
    while izquierdo < derecho:
        if arreglo[izquierdo] == arreglo[derecho]:
            break
        temporal = arreglo[izquierdo]
        arreglo[izquierdo] = arreglo[derecho]
        arreglo[derecho] = temporal
        izquierdo += 1
        derecho -= 1
    
    return arreglo

numeros = [10, 20, 30, 40, 50]
resultado = punteros(numeros)
print(resultado)

        
        
        
                