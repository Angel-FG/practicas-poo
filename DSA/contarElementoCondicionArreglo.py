def contarElemento(arreglo):
    longitud = len(arreglo)
    vecesVisto = 0
    indice = 0
    
    while indice < longitud:
        if arreglo[indice] > 200:
            vecesVisto += 1
        indice += 1
        
    return vecesVisto

arreglo = [150, 220, 190, 300, 280]

visto = contarElemento(arreglo)
print(visto)