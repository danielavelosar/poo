import random
def busqueda_lineal(largo_del_array, numero):
    """ Crea un array de numeros random y busca el que diga la persona
    """
    match=False
    array=[random.randint(0,100) for i in range (largo_del_array)]
    print(array)
    if numero in array:
        match =True
        
    else: match=False
        
    return match



if __name__ == "__main__":
    largo_del_array=int(input("qué tan grande quieres que sea la lista?"))
    numero=int(input("qué número buscas?"))
    encontrado=busqueda_lineal(largo_del_array, numero)
    print(f'{numero} {"está" if encontrado else "no está" } en el arreglo')
    #busqueda_lineal(largo_del_array, numero)
    
    
