def numerosPositivos(arreglo):
    longitud = len(arreglo)
    indice = 0
    listaVacia = []
    conteoPositivos = 0
    sumaPositivos = 0
    mayorPositivo = 0
    posicionMayorPositivo = 0
    
    while indice < longitud:
        if arreglo[indice] > 0:
            listaVacia.append(arreglo[indice])
            conteoPositivos += 1
            sumaPositivos += arreglo[indice]
            
        if arreglo[indice] > mayorPositivo:
            mayorPositivo = arreglo[indice]
            posicionMayorPositivo= indice
            
        indice += 1
    resultado = f"La lista de solo positivos es {listaVacia} | La cantidad de positivos es de {conteoPositivos} | La suma de los positivos es de {sumaPositivos} | El mayor positivo es {mayorPositivo} | la posicion de mayor positivo es de {posicionMayorPositivo}"    
    return resultado
numeros = [4, -2, 7, -5, 0, 8, -1, 3]

resultado = numerosPositivos(numeros)
print(resultado)