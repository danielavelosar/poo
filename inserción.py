import random 
def ordenamiento_por_inserción(lista, tamaño_de_la_lista):
    lista_ordenada=[lista[0]]
    bigger=False
    for i in range (len(lista)-1):
        valor_actual=lista_ordenada[i]
        valor_para_agregar=lista[i+1]
        
        if valor_para_agregar> valor_actual:
            lista_ordenada.append(valor_para_agregar) 
  
            print(f"lista ordenada= {lista_ordenada}")

        else: 
            for j in range (len(lista_ordenada)-1,-1,-1):
                valor_actual_en_la_lista=lista_ordenada[j]
                if valor_para_agregar > valor_actual_en_la_lista:
                    lista_ordenada.insert(j+1,valor_para_agregar)
                    bigger = True
                    print(f"lista ordenada= {lista_ordenada}")
                    break
            if bigger==False:
                lista_ordenada.insert(0,valor_para_agregar)
            else:
                bigger=False    


            print(lista_ordenada)
    

    return lista_ordenada



if __name__ == "__main__":
    tamaño_de_la_lista =int(input("¿de qué tamaño desea la lista?"))
    lista = [random.randint(0,100) for i in range (tamaño_de_la_lista)]
    print(lista)
    lista_ordenada=ordenamiento_por_inserción(lista, tamaño_de_la_lista)
    print(lista_ordenada)