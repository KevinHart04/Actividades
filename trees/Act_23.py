from Tree import AVLTree
from collections import Counter
from queue import SimpleQueue

class CreatureTree(AVLTree):
    """
    Extiende AVLTree para manejar criaturas mitológicas.
    Cada nodo almacena:
    - value: nombre de la criatura
    - data: diccionario con keys:
        - 'defeated_by': nombre del héroe o dios que la derrotó
        - 'captured_by': nombre del héroe o dios que la capturó (puede ser None)
        - 'description': breve descripción de la criatura
    """
    def insert_creature(self, name, defeated_by=None, captured_by=None, description=""):
        self.insert(name, {"defeated_by": defeated_by, "captured_by": captured_by, "description": description})
        
creatures_data = [
    ("Ceto", None, None, ""),
    ("Tifón", "Zeus", None, ""),
    ("Equidna", "Argos Panoptes", None, ""),
    ("Dino", None, None, ""),
    ("Pefredo", None, None, ""),
    ("Enio", "Heracles", None, ""),
    ("Escila", None, None, ""),
    ("Caribdis", None, None, ""),
    ("Euríale", None, None, ""),
    ("Esteno", "Minotauro de Creta", None, ""),
    ("Medusa", "Perseo", None, ""),
    ("Ladón", "Heracles", None, ""),
    ("Águila del Cáucaso", None, None, ""),
    ("Quimera", "Belerofonte", None, ""),
    ("Hidra de Lerna", "Heracles", None, ""),
    ("León de Nemea", "Heracles", None, ""),
    ("Esfinge", "Edipo", None, ""),
    ("Dragón de la Cólquida", None, None, ""),
    ("Cerbero", None, None, ""),
    ("Cerda de Cromión", "Teseo", None, ""),
    ("Ortro", "Heracles", None, ""),
    ("Toro de Creta", "Teseo", None, ""),
    ("Jabalí de Calidón", "Atalanta", None, ""),
    ("Carcinos", None, None, ""),
    ("Cloto", None, None, ""),
    ("Láquesis", None, None, ""),
    ("Átropos", None, None, ""),
    ("Minotauro de Creta", "Teseo", None, ""),
    ("Harpías", None, None, ""),
    ("Argos Panoptes", "Hermes", None, ""),
    ("Aves del Estínfalo", None, None, ""),
    ("Talos", "Medea", None, ""),
    ("Sirenas", None, None, ""),
    ("Pitón", "Apolo", None, ""),
    ("Cierva de Cerinea", None, None, ""),
    ("Basilisco", None, None, ""),
    ("Jabalí de Erimanto", None, None, "")
]


tree = CreatureTree()
for name, defeated, captured, desc in creatures_data:
    tree.insert_creature(name, defeated_by=defeated if defeated != "-" else None, captured_by=captured, description=desc)
    


print("\n=== Listado inorden de criaturas y quien las derrotó ===")
for name, data in tree.in_order():
    print(f"{name} - Derrotado por: {data['defeated_by']}")


talos = tree.search("Talos")
if talos:
    print("\n=== Información de Talos ===")
    print(f"Nombre: {talos.value}")
    print(f"Derrotado por: {talos.data['defeated_by']}")
    print(f"Capturado por: {talos.data['captured_by']}")
    print(f"Descripción: {talos.data['description']}")


counter = Counter()
for _, data in tree.in_order():
    if data['defeated_by']:
        for hero in data['defeated_by'].split(","):
            counter[hero.strip()] += 1

top3 = counter.most_common(3)
print("\n=== Top 3 héroes que derrotaron más criaturas ===")
for hero, count in top3:
    print(f"{hero}: {count} criaturas")
    
    


print("\n=== Criaturas derrotadas por Heracles ===")
for name, data in tree.in_order():
    if data['defeated_by'] and "Heracles" in data['defeated_by']:
        print(name)


print("\n=== Criaturas no derrotadas ===")
for name, data in tree.in_order():
    if not data['defeated_by']:
        print(name)


for creature in ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]:
    node = tree.search(creature)
    if node:
        node.data['captured_by'] = "Heracles"
        
        


search_term = "Dragón"
found = tree.proximity_search(search_term)
print(f"\n=== Criaturas que contienen '{search_term}' ===")
for name, data in found:
    print(name)



tree.delete("Basilisco")
tree.delete("Sirenas")



aves = tree.search("Aves del Estínfalo")
if aves:
    aves.data['defeated_by'] = "Heracles (varias derrotas)"


ladon = tree.search("Ladón")
if ladon:
    data = ladon.data
    tree.delete("Ladón")
    tree.insert_creature("Dragón Ladón", data['defeated_by'], data['captured_by'], data['description'])




print("\n=== Listado por nivel ===")
q = SimpleQueue()
if tree.root:
    q.put(tree.root)
while not q.empty():
    node = q.get()
    print(f"{node.value} - Derrotado por: {node.data['defeated_by']}")
    if node.left:
        q.put(node.left)
    if node.right:
        q.put(node.right)

print("\n=== Criaturas capturadas por Heracles ===")
for name, data in tree.in_order():
    if data['captured_by'] == "Heracles":
        print(name)
