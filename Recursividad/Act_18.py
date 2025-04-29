def recorrer_matriz(matriz, fila=0, columna=0):
    if fila >= len(matriz):
        return
    
    if columna >= len(matriz[fila]):
        print()  
        recorrer_matriz(matriz, fila + 1, 0)
        return
    
    print(matriz[fila][columna], end=" ")
    
    recorrer_matriz(matriz, fila, columna + 1)


def main():
    matriz_ejemplo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    recorrer_matriz(matriz_ejemplo)

if __name__ == "__main__":
    main()