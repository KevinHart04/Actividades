def inverir_numero(numero):
    if numero == 0:
        return "0"
    else :
        inverso = 0
        while numero > 0:
            ultimo = numero % 10
            inverso = inverso * 10 + ultimo
            numero = numero // 10
    return inverso


entrada = input("[*] Ingrese un número entero: ")
resultado = inverir_numero(int(entrada))
print(f'[*] El número {entrada} invertido es: {resultado}')