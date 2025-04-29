def suma_hasta_n(n):
    """
    Calcula la suma de todos los números enteros comprendidos entre 0 y un número entero positivo dado.
    """
    if n < 0:
        raise ValueError("[!] El número debe ser un entero positivo.")
    return n * (n + 1) // 2

def main():
    """
    Función principal que solicita un número entero positivo al usuario y calcula la suma de los números entre 0 y ese número.
    """
    numero = int(input("[*] Introduce un número entero positivo: "))
    try:
        resultado = suma_hasta_n(numero)
        print(f"[=] La suma de los números entre 0 y {numero} es: {resultado}")
    except ValueError as e: 
        print(e)
        
if __name__ == "__main__":
    main()