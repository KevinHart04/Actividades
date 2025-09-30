from Tree import AVLTree

# -----------------------------
# - Crear árbol MCU
# -----------------------------

mcu_tree = AVLTree()
personajes = [
    ("Iron Man", True),
    ("Thanos", False),
    ("Doctor Strange", True),
    ("Capitán América", True),
    ("Loki", False),
    ("Ultron", False),
    ("Spider-Man", True),
    ("Scarlet Witch", True),
    ("Hela", False),
    ("Captain Marvel", True)
]

for nombre, es_heroe in personajes:
    mcu_tree.insert(nombre, {"is_hero": es_heroe})

# -----------------------------
# - Villanos alfabéticamente
# -----------------------------
print("=== Villanos alfabéticamente ===")
for nombre, datos in mcu_tree.in_order():
    if not datos["is_hero"]:
        print(nombre)

# -----------------------------
# - Héroes que empiezan con C
# -----------------------------
print("\n=== Héroes que empiezan con 'C' ===")
for nombre, datos in mcu_tree.in_order():
    if datos["is_hero"] and nombre.startswith("C"):
        print(nombre)

# -----------------------------
# - Cantidad de superhéroes
# -----------------------------
num_heroes = sum(1 for _, datos in mcu_tree.in_order() if datos["is_hero"])
print(f"\nCantidad de superhéroes: {num_heroes}")

# -----------------------------
# - Corregir Doctor Strange
# -----------------------------
proximos = mcu_tree.proximity_search("Dr")
for nombre, datos in proximos:
    mcu_tree.insert("Doctor Strange", datos)
    mcu_tree.delete(nombre)

print("\nDoctor Strange corregido en el árbol.")

# -----------------------------
# - Héroes en orden descendente
# -----------------------------
print("\n=== Héroes en orden descendente ===")
for nombre, datos in mcu_tree.in_order(reverse=True):
    if datos["is_hero"]:
        print(nombre)

# -----------------------------
# - Bosque: Héroes y Villanos
# -----------------------------
heroes_tree = AVLTree()
villanos_tree = AVLTree()

for nombre, datos in mcu_tree.in_order():
    if datos["is_hero"]:
        heroes_tree.insert(nombre, datos)
    else:
        villanos_tree.insert(nombre, datos)

print(f"\nCantidad de héroes: {heroes_tree.size()}")
print(f"Cantidad de villanos: {villanos_tree.size()}")

print("\n=== Héroes ordenados ===")
for nombre, _ in heroes_tree.in_order():
    print(nombre)

print("\n=== Villanos ordenados ===")
for nombre, _ in villanos_tree.in_order():
    print(nombre)
