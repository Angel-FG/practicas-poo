def valorAlto(arreglo):
    valorMasAlto = 0
    longitud = len(arreglo)
    indice = 0
    
    while indice < longitud:
        #   0 < 5 -> 5 es la longitud del arreglo
        if valorMasAlto < arreglo[indice]: #El valor del arreglo en esa posicion
            valorMasAlto = arreglo[indice]
        indice += 1
    return valorMasAlto
    
arreglo = [5, 4, 2, 8, 9, 20, 17]

valor = valorAlto(arreglo)
print(valor)