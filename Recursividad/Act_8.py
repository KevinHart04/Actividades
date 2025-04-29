def Convertir_a_binario(numero):
    if numero == 0:
        return "0"
    else :
        binario = []
        while numero > 0:
            binario.append(str(numero % 2))
            numero = numero // 2
    return binario[::-1]


entrada = input("[*] Ingrese un número entero: ")
resultado = Convertir_a_binario(int(entrada))
print(f'[*] El número {entrada} en binario es: {"".join(resultado)}')