import random
def busqueda_binaria(array, numero, inicio, fin):
    """ Crea un array de numeros random ordenados y busca por busqueda binaria el que diga la persona
    """
    print(f'buscando {numero} entre {array[inicio]} y {array[fin-1]} ')
    if inicio> fin:
        return False
    mitad=(inicio+fin)//2
    if array[mitad]==numero:
        return True
    elif array[mitad]>numero:
        
        return busqueda_binaria(array, numero, inicio, mitad-1)
            
    else:
        
        return busqueda_binaria(array, numero, mitad+1, fin)       


if __name__ == "__main__":
    largo_del_array=int(input("qué tan grande quieres que sea la lista?"))
  
    numero=int(input("qué número buscas?"))
    array = sorted([random.randint(0,100) for i in range (largo_del_array)])
    print(array) 
    encontrado=busqueda_binaria(array, numero, 0, len(array))

    print(f'{numero} {"está" if encontrado else "no está" } en el arreglo')
    #busqueda_lineal(largo_del_array, numero)