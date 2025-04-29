from math import log


def logaritmo(a:int, b:int) -> float:
    return log(a,b)


def main ():
    a:int = int(input("[*] Ingrese el Argumento del logaritmo: "))
    b:int = int(input("[*] Ingrese la base del logaritmo: "))
    resultado:float = logaritmo(a,b)
    print(f"[=] el logaritmo en base {a} de {b} es {resultado}")


if __name__ == "__main__":
    main()