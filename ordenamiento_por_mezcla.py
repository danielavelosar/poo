import random 
def ordenamiento_por_mezcla(lista):
    medio=0
    
    if len(lista)>1 :
        medio=(len(lista))//2
        izquierda=lista[:medio]
        derecha=lista[medio:]
        print (F'izquierda {izquierda} {"-"*5} derecha {derecha}')
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        #Iteradores en las sublistas 
        i=0
        j=0
        #Iteradores en la lista principal
        k=0
        while i<len(izquierda) and j<len(derecha):
            if izquierda[i]< derecha[j] :
                lista[k]=izquierda[i]
                i+=1
            else:
                lista[k]=derecha[j]
                j+=1
            k+=1
        while i<len(izquierda):
            lista[k]=izquierda[i]
            i+=1
            k+=1
        while j<len(derecha):
            lista[k]= derecha[j]
            j+=1
            k+=1            
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)


    

    

                
    return lista

if __name__ == "__main__":
    tamaño_de_la_lista =int(input("¿de qué tamaño desea la lista?"))
    lista = [random.randint(0,100) for i in range (tamaño_de_la_lista)]
    print(lista)
    print ("-"*50)
    lista_ordenada=ordenamiento_por_mezcla(lista)
    print(lista_ordenada)