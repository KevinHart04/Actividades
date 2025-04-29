def producto(a:int, b:int) -> int:
    """
    Calcula el producto de dos números enteros utilizando la suma repetida.
    """
    if b == 0:
        return 0
    elif b < 0:
        return -producto(a, -b)
    else:
        return a + producto(a, b - 1)

def main():
    a:int = int(input("[*] Ingrese el primer número: "))
    b:int = int(input("[*] Ingrese el segundo número: "))
    resultado:int = producto(a,b)
    print(f"El producto de {a} multiplicado por {b} es = {resultado}")
    
if __name__ == "__main__":
    main()