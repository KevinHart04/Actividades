# colores.py
'''Esta Libreria esta creada para modificar el color de los outputs de la consola'''
# Códigos ANSI para colores y estilos
RESET = "\033[0m"
NEGRITA = "\033[1m"

# Colores de texto
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"
NEGRO = "\033[30m"


FONDO_ROJO = "\033[41m"
FONDO_VERDE = "\033[42m"
FONDO_AMARILLO = "\033[43m"
FONDO_AZUL = "\033[44m"
FONDO_MAGENTA = "\033[45m"
FONDO_CIAN = "\033[46m"
FONDO_BLANCO = "\033[47m"

def color(texto, color):
    """Aplica color al texto."""
    return f"{color}{texto}{RESET}"
