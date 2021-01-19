import random 
def ordenamiento_por_burbuja(lista, tamaño_de_la_lista):
    for i in range (tamaño_de_la_lista):
        for j in range (tamaño_de_la_lista-i-1):
            if lista[j]> lista[j+1]:
                lista[j], lista[j+1]= lista[j+1], lista[j]
                
    return lista

if __name__ == "__main__":
    tamaño_de_la_lista =int(input("¿de qué tamaño desea la lista?"))
    lista = [random.randint(0,100) for i in range (tamaño_de_la_lista)]
    print(lista)
    lista_ordenada=ordenamiento_por_burbuja(lista, tamaño_de_la_lista)
    print(lista_ordenada)