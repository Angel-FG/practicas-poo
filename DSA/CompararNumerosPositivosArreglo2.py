def arrays(arreglo):
    longitud = len(arreglo)
    indice = 0
    cantidadPares = 0
    valorPar = []
    sumaPares = 0
    menorPar = float('inf')
 
    PosicionMenor = 0
    
    while indice < longitud:
        if arreglo[indice] % 2 == 0:
            valorPar.append(arreglo[indice])
            cantidadPares += 1
            sumaPares += arreglo[indice] 
            if menorPar > arreglo[indice]:
                menorPar = arreglo[indice]
                PosicionMenor = indice
        indice += 1
        
    total = f"La lista de numeros pares es de {valorPar}, la cantidad de pares es {cantidadPares} la suma de los pares es de {sumaPares} el numero menor par es {menorPar} la posicion del menor par es {PosicionMenor}"
    return total
numeros = [5, 18, 7, 24, 3, 16, 9, 12]
resultado = arrays(numeros)
print(resultado)