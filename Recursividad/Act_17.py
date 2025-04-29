def lista_invertida(lista:list) -> list:
    lista_alrevez = []
    if lista == []:
        return lista_alrevez
    else:
        lista_alrevez.append(lista[-1])
        lista_alrevez += lista_invertida(lista[:-1])
        return lista_alrevez

def main():
    """
    Función principal que solicita al usuario una lista de números y muestra la lista invertida.
    """
    lista = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()]
    resultado = lista_invertida(lista)
    if resultado == []:
        print("La lista está vacía.")
    else:
        print(f"La lista original es: {lista}")
        print(f"La lista invertida es: {resultado}")


if __name__ == "__main__":
    main()