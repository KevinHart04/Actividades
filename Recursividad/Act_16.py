def sucesion_geometrica(n, a1=2, r=-3):
    """
    Función recursiva para calcular el valor de an en una sucesión geométrica.
    """
    if n == 1:
        return a1
    return r * sucesion_geometrica(n - 1, a1, r)

def visualizar_sucesion(n, a1=2, r=-3):
    """
    Función para visualizar todos los valores de la sucesión geométrica desde a1 hasta an.
    """
    for i in range(1, n + 1):
        print(f"a{i} = {sucesion_geometrica(i, a1, r)}")

# Ejemplo de uso
if __name__ == "__main__":
    n = int(input("Ingrese el número de términos de la sucesión a calcular: "))
    visualizar_sucesion(n)