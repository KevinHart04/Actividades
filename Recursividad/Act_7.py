def serie(n:int) -> float:
    if n == 1:
        return 1
    else:
        return (1 / n) + serie(n-1)

def main():
    n:int = int(input("[*] Ingrese la cantidad de veces que desea calcular la serie: "))
    if n <= 0:
        raise ValueError("[!] El número debe ser un entero positivo.")
    elif n >= 995:
        raise ValueError("[!] El número debe ser menor que 995.")
    else:
        resultado:float = serie(n)
        print(f"[=] El resultado de la serie es: {resultado}")

if __name__ == "__main__":
    main()


