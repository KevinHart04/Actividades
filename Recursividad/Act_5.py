import colores
import re

def Romano_a_decimal(romano):
    """Convierte un número romano a decimal, validando el formato antes de la conversión."""    
    valores = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }
    
    romano = romano.upper()
    
    if not romano:          # - verifica si el numero dado no esta vacío, si no lo esta comienza a convertir.
        raise ValueError(colores.color("[x] Nada ingresado", colores.ROJO))
    
    def validar(indice):
        '''Valida el número romano ingresado'''


        if indice >= len(romano):         # - Verifica si el caracter a revisar es igual o mayor al último caracter del numero ingresado.
            return True                   # - Si se cumple cualquiera detiene la ejecución.


        patron = r"(IIII|XXXX|CCCC|MMMM|VV|LL|DD)"       # - Corrobora que se cumpla el formato de los numeros romanos evitando
        if re.search(patron, romano):                    # - Las repeticiones de algunas letras.
            raise ValueError(colores.color("[*] Formato inválido", colores.ROJO))

        
        if romano[indice] not in valores:                # - Corrobora que los carácteres ingresados se encuentren en el diccionario dado arriba.
            raise ValueError(colores.color(f"[*] Carácter invalido en número romano: '{romano[indice]}'", colores.ROJO))
        
        return validar(indice + 1)
    
    validar(0)
    

    def convertir(indice):
        '''Convierte la cadena ingresada a numeros decimales'''
        if indice == len(romano):                       # - Termina la recursión al llegar al final del número romano.
            return 0
        actual = valores[romano[indice]]                # - Obtiene el valor decimal del símbolo actual.    
        
        if indice + 1 < len(romano):                    # - Valida si hay letras siguientes y les asigna un valor.
            siguiente = valores[romano[indice + 1]]
            
            if actual < siguiente:                      # - Aplica regla de sustracción (ej: IX = 9 en lugar de 11)
                return -actual + convertir(indice + 1)
            
        return actual + convertir(indice + 1)           # - De lo contrario sigue con la conversion normalmente.

    
    
    return convertir(0)


def main():
    entrada = input(colores.color("[*] Ingresa un numero romano: ", colores.VERDE))
    try:
        resultado = Romano_a_decimal(entrada)
        print(colores.color(f"[*] El numero romano ingresado en decimal es '{resultado}'", colores.AMARILLO))
    except ValueError as e:
        print(colores.color(f"Error: '{e}'", colores.ROJO))
        

if __name__ == "__main__":
    main()
        