import random
import stack
import colores as color

class Personajes:
    def __init__(self, nombre: str, apariciones: int):
        self.nombre = nombre
        self.apariciones = apariciones
    
    def __str__(self):
        return color.color(f"| {self.nombre:<35} | {self.apariciones:^15} |", color.MAGENTA)

# - Esta hecho con random para que cada vez que se ejecute el programa, los personajes tengan un número diferente de apariciones.
mcu_characters = {
    "Vengadores": [
        "Iron Man", "Capitán América (Steve Rogers)", "Thor", "Hulk",
        "Viuda Negra", "Ojo de Halcón", "Bruja Escarlata", "Visión",
        "Ant-Man", "Wasp", "Spider-Man", "Doctor Strange", "Capitana Marvel",
        "Falcon (Sam Wilson)", "Soldado del Invierno", "War Machine"
    ],
    "Guardianes de la Galaxia": [
        "Star-Lord", "Gamora", "Drax", "Rocket", "Groot", "Mantis", "Nébula"
    ],
    "Wakanda": [
        "Black Panther", "Shuri", "Okoye", "Nakia", "Ramonda"
    ],
    "S.H.I.E.L.D. y aliados": [
        "Nick Fury", "Maria Hill", "Phil Coulson", "Peggy Carter", "Sharon Carter"
    ],
    "Maestros de las Artes Místicas": [
        "Doctor Strange", "Anciana", "Wong", "Karl Mordo"
    ],
    "Multiverso y nuevos héroes": [
        "Shang-Chi", "Yelena Belova", "Kate Bishop", "Moon Knight",
        "Ms. Marvel", "She-Hulk", "Namor", "Reed Richards", "Sue Storm",
        "Deadpool", "Wolverine"
    ],
    "Otros aliados": [
        "Hank Pym", "Janet van Dyne", "Luis", "Darcy Lewis",
        "Jane Foster", "Erik Selvig", "Loki"
    ],
    "Villanos": [
        "Thanos", "Ultron", "Loki", "Hela", "Killmonger", "Red Skull",
        "Ronan", "Mandarín (Wenwu)", "Agatha Harkness", "Mysterio",
        "Vulture"
    ]
}


def crear_pila_personajes():
    pila = stack.Stack()
    for grupo, personajes in mcu_characters.items():
        for personaje in personajes:
            apariciones = random.randint(1, 35)
            pila.push(Personajes(personaje, apariciones))
    return pila

def groot_and_rocket_position(pila: stack.Stack):
    aux = stack.Stack()
    pos = 0
    groot_pos = -1
    rocket_pos = -1

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.nombre == "Groot":
            groot_pos = pos
        elif personaje.nombre == "Rocket":
            rocket_pos = pos
        
        aux.push(personaje)
        pos += 1
    
    while aux.size() > 0:
        pila.push(aux.pop())
        
    return groot_pos, rocket_pos


def more_than_5_appearances(pila: stack.Stack):
    pila_de_5 = stack.Stack()
    aux = stack.Stack()
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.apariciones > 5:
            pila_de_5.push(personaje)
            aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())
    return pila_de_5

def viuda_negra_apariciones(pila: stack.Stack):
    viuda_negra = 0
    aux = stack.Stack()
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.nombre == "Viuda Negra":
            viuda_negra = personaje.apariciones
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())
    return viuda_negra

def c_d_g_names(pila: stack.Stack):
    pila_aux = stack.Stack()
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.nombre.startswith(("C", "D", "G")):
            pila_aux.push(personaje)
    return pila_aux


def main():
    pila = crear_pila_personajes()
    print(color.color('\n[*] Personajes y sus apariciones:\n', color.AZUL))
    print(color.color(f"| {'Nombre':<35} | {'Apariciones':^15} |", color.AMARILLO))
    
    
    for i in range(pila.size()):
        print(f'{i} {pila.show()}')
    
    pila_mas_5_apariciones = more_than_5_appearances(pila)
    print(color.color('\n[*] Personajes con más de 5 apariciones:\n', color.NEGRITA))
    while pila_mas_5_apariciones.size() > 0:
        personaje = pila_mas_5_apariciones.pop()
        print(f'{personaje.nombre} - {personaje.apariciones} apariciones')

    groot_pos, rocket_pos = groot_and_rocket_position(pila)
    print(color.color(f'\n[+] Groot está en la posición {groot_pos}', color.VERDE))
    print(color.color(f"[+] Rocket está en la posición {rocket_pos}", color.VERDE))

    apariciones_viuda_negra = viuda_negra_apariciones(pila)
    print(color.color(f"\n[*] Viuda Negra aparece en {apariciones_viuda_negra} películas", color.VERDE))
    
    pila_c_d_g = c_d_g_names(pila)
    print(color.color('\n[*] Personajes que comienzan con C, D o G:\n', color.AZUL))
    while pila_c_d_g.size() > 0:
        personaje = pila_c_d_g.pop()
        print(personaje.nombre)

if __name__ == "__main__":
    main()

