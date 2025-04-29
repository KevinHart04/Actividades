def Fibonacci(n):
    '''Calcula el n-ésimo número de Fibonacci de forma recursiva'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    
def main():
    '''Función principal'''
    n = int(input("Ingrese el número de Fibonacci que desea calcular: "))
    resultado = Fibonacci(n)
    print(f"El {n}-ésimo número de Fibonacci es: {resultado}")
    

if __name__ == "__main__":
    main()