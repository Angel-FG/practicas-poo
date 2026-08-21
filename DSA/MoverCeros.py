def ceros(arreglo):
    longitud = len(arreglo)
    izquierdo = 0 #Ancla el que se queda en la izquierda esperando numeros validos
    derecho = 0 #Puntero explorador que avanza hacia el final de la lista
    while derecho < longitud:
        if longitud == 1:
            return arreglo[izquierdo]
        
        if arreglo[derecho] != 0:
            temporal = arreglo[izquierdo]
            arreglo[izquierdo] = arreglo[derecho]
            arreglo[derecho] = temporal
        
            izquierdo += 1
        derecho += 1
    return arreglo

nums = [0, 1, 0, 3, 12]
resultado = ceros(nums)
print(resultado)