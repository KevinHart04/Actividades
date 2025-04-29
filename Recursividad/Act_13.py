def mcd(a,b):
    """
    Calcula el máximo común divisor de dos números enteros positivos a y b.
    """
    while b != 0:
        a, b = b, a % b
    return a


def main():
    """
    Función principal que solicita al usuario dos números enteros positivos y calcula su MCM.
    """
    try:
        a = abs(int(input("Introduce el primer número: ")))
        b = abs(int(input("Introduce el segundo número entero: ")))
        resultado = abs(a * b) // mcd(a, b)
        # El MCM se calcula como el producto de los números dividido por su MCD
        print(f"El mínimo común múltiplo de {a} y {b} es: {resultado}")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()