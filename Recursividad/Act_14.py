def Sumar_numeros(numero):
    total = 0
    while numero > 0:
        total += numero % 10
        numero = numero // 10
    return total

entrada = input("[*] Ingrese un número: ")
resultado = Sumar_numeros(int(entrada))
print(f'[*] La suma de los dígitos del número {entrada} es: {resultado}')
