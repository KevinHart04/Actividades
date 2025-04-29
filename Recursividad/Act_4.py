def potencia(a,b):
    if b == 0:
        return 1
    else:
        return a**b

def main():
    a:int = int(input("[*] Ingrese el primer número: "))
    b:int = int(input("[*] Ingrese el segundo número: "))
    resultado = potencia(a,b)
    print(f"{a} elevado a {b} es igual {resultado}")


if __name__ == "__main__":
    main()