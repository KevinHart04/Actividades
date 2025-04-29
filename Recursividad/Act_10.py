def contar_digitos(numero):
    '''Cuenta la cantidad de dígitos en un número entero'''
    if numero < 0:
        numero = -numero
    if numero == 0:
        return 1
    return len(str(numero))

def main():
    numero = int(input("[*] Ingrese un número: "))
    resultado:int = contar_digitos(numero)
    print(f"[=] El número tiene {resultado} dígito/s.")


if __name__ == "__main__":
    main()