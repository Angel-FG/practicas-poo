def puntero(arreglo, objet):
    izquierdo = 0
    derecho = len(arreglo) - 1
    objetivo = objet
    
    while izquierdo < derecho:
        valorActual = arreglo[izquierdo] + arreglo[derecho]
        if valorActual == objetivo:
            return [izquierdo, derecho]
        elif valorActual > objetivo:
            derecho -= 1
        elif valorActual < objetivo:
            izquierdo += 1
        else:
            print("El numero no es posible formarlo")

numeros = [2, 7, 11, 15, 20]
objetivo = 18

total = puntero(numeros, objetivo)
print(total)       
       