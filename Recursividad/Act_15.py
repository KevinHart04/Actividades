import math

def raiz_cuadrada(numero) -> float:
    """Calcula la raíz cuadrada de un número."""
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(numero)

def main():
    """Función principal que solicita al usuario un número y calcula su raíz cuadrada."""
    numero = int(input("Introduce un número para calcular su raíz cuadrada: "))
    resultado = raiz_cuadrada(numero)
    print(f"La raíz cuadrada de {numero} es: {resultado:.2f}")


if __name__ == "__main__":
    main()