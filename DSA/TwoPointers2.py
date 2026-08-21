def puntero(arreglo):
    izquierdo = 0
    derecho = len(arreglo) - 1
    
    while izquierdo < derecho:
        #Se busca que en la lista el valor sea identico
        #[1, 2, 3, 4, 5] False
        #[1, 2, 3, 2, 1] True
        
        if arreglo[izquierdo] == arreglo[derecho]:
            izquierdo += 1
            derecho -= 1
        else:
            return False
    return True

numeros1 = [1, 2, 3, 4, 5]
numeros2 = [1, 2, 3, 2, 1]

total = puntero(numeros2)
print(total)