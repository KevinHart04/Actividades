from lista import List
from SuperHeroesData import superheroes


def cargar_superheroes(lista, dataset):
    """
    Carga los diccionarios del dataset en la lista.
    """
    for hero in dataset:
        lista.append(hero)


if __name__ == "__main__":
    # --- inicializamos la lista ---
    lista = List()

    # definimos los criterios de búsqueda (para que funcione el search/delete_value)
    lista.add_criterion("name", lambda x: x["name"])
    lista.add_criterion("first_appearance", lambda x: x["first_appearance"])

    # cargamos los datos
    cargar_superheroes(lista, superheroes)

    # a. eliminar el nodo que contiene la información de Linterna Verde
    eliminado = lista.delete_value("Green Lantern", key_value="name")
    print("a) Eliminado:", eliminado)

    # b. mostrar el año de aparición de Wolverine
    idx = lista.search("Wolverine", search_key="name")
    if idx is not None:
        print("b) Wolverine apareció en:", lista[idx]["first_appearance"])

    # c. cambiar la casa de Dr. Strange a Marvel
    idx = lista.search("Dr. Strange", search_key="name")
    if idx is not None:
        lista[idx]["publisher"] = "Marvel"
        print("c) Casa de Dr. Strange actualizada a Marvel")

    # d. mostrar superhéroes con “traje” o “armadura” en la biografía
    print("d) Superhéroes con 'traje' o 'armadura' en la bio:")
    for hero in lista:
        bio = hero["short_bio"].lower()
        if "traje" in bio or "armadura" in bio:
            print("   -", hero["name"])

    # e. nombre y casa de los superhéroes anteriores a 1963
    print("e) Superhéroes con aparición antes de 1963:")
    for hero in lista:
        if hero["first_appearance"] < 1963:
            print(f"   - {hero['name']} ({hero['publisher']})")

    # f. mostrar la casa de Capitana Marvel y Mujer Maravilla
    for nombre in ["Captain Marvel", "Wonder Woman"]:
        idx = lista.search(nombre, search_key="name")
        if idx is not None:
            print(f"f) {nombre} pertenece a:", lista[idx]["publisher"])

    # g. mostrar toda la información de Flash y Star-Lord
    for nombre in ["Flash", "Star-Lord"]:
        idx = lista.search(nombre, search_key="name")
        if idx is not None:
            print(f"g) Info de {nombre}:", lista[idx])

    # h. listar superhéroes que comienzan con B, M o S
    print("h) Superhéroes que empiezan con B, M o S:")
    for hero in lista:
        if hero["name"].startswith(("B", "M", "S")):
            print("   -", hero["name"])

    # i. determinar cuántos superhéroes hay de cada casa
    contador = {}
    for hero in lista:
        casa = hero["publisher"]
        contador[casa] = contador.get(casa, 0) + 1
    print("i) Cantidad de héroes por casa:", contador)
