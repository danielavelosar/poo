def mochila (tamaño_de_mochila, pesos, valores, n):
    #siempre agregar el caso base
    if n==0 or tamaño_de_mochila==0:
        return 0
    if tamaño_de_mochila< pesos[n-1]: #si la mochila es más pequeña que el peso
        return mochila(tamaño_de_mochila, pesos, valores, n-1)
    return max(valores[n-1]+mochila (tamaño_de_mochila-pesos[n-1], pesos, valores, n-1),mochila (tamaño_de_mochila, pesos, valores, n-1))
    #max compara dos cosas separadas por una coma, valores es lo  que quiero optimizar

if __name__== "__main__":
    pesos =[20, 10, 30] #kilos
    valores =[200, 100, 50] #dólares
    tamaño_de_mochila=30 #kilos
    n=len(valores) #lo que quiero optimizar, es importante porque con esto se aplica la recursividad.
    resultado=mochila(tamaño_de_mochila, pesos, valores, n) 
    print(resultado)
