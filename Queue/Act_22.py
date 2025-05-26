from cola import Queue
from colores import color, VERDE, AMARILLO, CIAN, MAGENTA, ROJO, NEGRITA, AZUL

def buscar_personaje_por_superheroe(cola: Queue, nombre_heroe: str) -> str:
    """
    Busca el nombre del personaje dado el nombre del superhéroe.
    """
    personaje = None
    for _ in range(cola.size()):
        datos = cola.move_to_end()
        if datos["superheroe"].lower() == nombre_heroe.lower():
            personaje = datos["personaje"]
    return personaje

def mostrar_superheroes_femeninos(cola: Queue) -> None:
    """
    Muestra los nombres de los superhéroes femeninos.
    """
    print(color("\nSuperhéroes femeninos:", VERDE))
    for _ in range(cola.size()):
        datos = cola.move_to_end()
        if datos["genero"] == "F":
            print(color(f"- {datos['superheroe']}", MAGENTA))

def mostrar_personajes_masculinos(cola: Queue) -> None:
    """
    Muestra los nombres de los personajes masculinos.
    """
    print(color("\nPersonajes masculinos:", CIAN))
    for _ in range(cola.size()):
        datos = cola.move_to_end()
        if datos["genero"] == "M":
            print(color(f"- {datos['personaje']}", AZUL))

def buscar_superheroe_por_personaje(cola: Queue, nombre_personaje: str) -> str:
    """
    Busca el nombre del superhéroe dado el nombre del personaje.
    """
    heroe = None
    for _ in range(cola.size()):
        datos = cola.move_to_end()
        if datos["personaje"].lower() == nombre_personaje.lower():
            heroe = datos["superheroe"]
    return heroe

def mostrar_nombres_con_s(cola: Queue) -> None:
    """
    Muestra los datos de los personajes o superhéroes cuyos nombres comienzan con S.
    """
    print(color("\nNombres que comienzan con 'S':", AMARILLO))
    for _ in range(cola.size()):
        datos = cola.move_to_end()
        if datos["personaje"].startswith("S") or datos["superheroe"].startswith("S"):
            print(color(f"- Personaje: {datos['personaje']} | Superhéroe: {datos['superheroe']} | Género: {datos['genero']}", CIAN))

def verificar_presencia_personaje(cola: Queue, nombre_personaje: str) -> None:
    """
    Verifica si un personaje está en la cola e imprime su superhéroe si está.
    """
    encontrado = False
    for _ in range(cola.size()):
        datos = cola.move_to_end()
        if datos["personaje"].lower() == nombre_personaje.lower():
            print(color(f"\n{nombre_personaje} está en la cola. Su superhéroe es: {datos['superheroe']}", VERDE))
            encontrado = True
            break
    if not encontrado:
        print(color(f"\n{nombre_personaje} no está en la cola.", ROJO))


# --- Ejemplo de uso ---
if __name__ == "__main__":
    cola_mcu = Queue()
    cola_mcu.arrive({"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
    cola_mcu.arrive({"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
    cola_mcu.arrive({"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
    cola_mcu.arrive({"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
    cola_mcu.arrive({"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})
    cola_mcu.arrive({"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"})
    cola_mcu.arrive({"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"})
    cola_mcu.arrive({"personaje": "Shuri", "superheroe": "Black Panther", "genero": "F"})

    # a. nombre del personaje de la superhéroe Capitana Marvel
    personaje = buscar_personaje_por_superheroe(cola_mcu, "Capitana Marvel")
    print(color(f"\nPersonaje de 'Capitana Marvel': {personaje}", NEGRITA + CIAN))

    # b. superheroes femeninos
    mostrar_superheroes_femeninos(cola_mcu)

    # c. personajes masculinos
    mostrar_personajes_masculinos(cola_mcu)

    # d. nombre del superhéroe del personaje Scott Lang
    heroe = buscar_superheroe_por_personaje(cola_mcu, "Scott Lang")
    print(color(f"\nSuperhéroe de Scott Lang: {heroe}", NEGRITA + CIAN))

    # e. datos de personajes o superhéroes que empiezan con S
    mostrar_nombres_con_s(cola_mcu)

    # f. verificar si Carol Danvers está y su superhéroe
    verificar_presencia_personaje(cola_mcu, "Carol Danvers")
