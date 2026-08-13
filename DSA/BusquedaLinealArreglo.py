# def busqueda(arreglo):
#     longitud = len(arreglo)
#     indice = 0
#     valorActual = 0
    
#     while indice < longitud:
#         valorActual = arreglo[indice]
#         indice += 1
        
#         if valorActual == 309:
#             return True
#         else:
#             pass
#     return False
# arreglo = [105, 204, 309, 401]
# visto = busqueda(arreglo)
# print(visto)
            
        
        
def busqueda(arreglo):
    longitud = len(arreglo)
    indice = 0
    
    while indice < longitud:
        if arreglo[indice] == 309:
             return True
        indice += 1

    return False
arreglo = [105, 204, 309, 401]
visto = busqueda(arreglo)
print(visto)
            
        