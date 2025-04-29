def funcion(x:int) -> float:
    if x == 1:
        return 2
    if x >= 2:
        return x + (1 / funcion(x - 1))

def main():
    x = int(input("Introduce un número entero positivo: "))
    resultado = funcion(x)
    print(f"El resultado de la función para x={x} es: {resultado:.2f}")

if __name__ == "__main__":
    main()

