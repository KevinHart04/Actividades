def Lista_Invertida(lista):
    return(lista[::-1])


Entrada = input("[*] Ingrese una lista de números separados por un [-]: ")
lista = [int(x) for x in Entrada.split('-')]
print("Lista original:", lista)
lista_invertida = Lista_Invertida(lista)
print("Lista invertida:", lista_invertida)
