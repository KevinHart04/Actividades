from graph import Graph  # Asumo que tu clase corregida está en graph.py
from colores import color, VERDE, AMARILLO, CIAN, MAGENTA, ROJO, NEGRITA, AZUL

def cargar_red(grafo: Graph) -> None:
    """
    Carga la topología de red del ejercicio en el grafo proporcionado.
    
    Cumple el punto (a): Carga nodos con su tipo.
    Cumple el punto (h): Al usar el grafo configurado como no dirigido.

    Args:
        grafo (Graph): Una instancia de la clase Graph vacía.
    """
    # Lista de dispositivos: (Nombre, Tipo)
    dispositivos = [
        ('Manjaro', 'PC'), ('Parrot', 'PC'), ('Fedora', 'PC'), ('Mint', 'PC'), ('Ubuntu', 'PC'),
        ('Arch', 'Notebook'), ('Debian', 'Notebook'), ('Red Hat', 'Notebook'),
        ('Guaraní', 'Servidor'), ('MongoDB', 'Servidor'),
        ('Switch 1', 'Switch'), ('Switch 2', 'Switch'),
        ('Router 1', 'Router'), ('Router 2', 'Router'), ('Router 3', 'Router'),
        ('Impresora', 'Impresora')
    ]

    print(color("--- Cargando Nodos (Punto A) ---", CIAN))
    for nombre, tipo in dispositivos:
        grafo.insert_vertex(nombre, other_values=tipo)

    # Lista de conexiones: (Origen, Destino, Peso)
    conexiones = [
        ('Manjaro', 'Switch 2', 40), ('Parrot', 'Switch 2', 12), 
        ('MongoDB', 'Switch 2', 5), ('Arch', 'Switch 2', 56), 
        ('Router 3', 'Switch 2', 61), ('Fedora', 'Router 3', 3),
        ('Guaraní', 'Router 3', 50), ('Router 1', 'Router 3', 43),
        ('Red Hat', 'Guaraní', 25), ('Router 2', 'Guaraní', 9),
        ('Router 1', 'Router 2', 37), ('Switch 1', 'Router 1', 29),
        ('Debian', 'Switch 1', 17), ('Ubuntu', 'Switch 1', 18),
        ('Mint', 'Switch 1', 80), ('Impresora', 'Switch 1', 22)
    ]

    print(color("--- Cargando Aristas ---", CIAN))
    for origen, destino, peso in conexiones:
        grafo.insert_edge(origen, destino, peso)


def obtener_info_dijkstra(pila_dijkstra, destino_buscado=None):
    """
    Procesa la pila devuelta por el algoritmo de Dijkstra para extraer información útil.
    
    Args:
        pila_dijkstra (Stack): La pila resultante de grafo.dijkstra().
        destino_buscado (str, optional): Si se especifica, filtra para devolver 
                                         la info solo de ese nodo.

    Returns:
        list: Lista de diccionarios [{'nodo': str, 'peso': int, 'padre': str}, ...]
              o un solo diccionario si se encontró el destino_buscado.
    """
    resultados = []

    
    while pila_dijkstra.size() > 0:
        # data estructura: [nombre_nodo, peso_acumulado, nombre_padre]
        data = pila_dijkstra.pop() 
        info = {'nodo': data[0], 'peso': data[1], 'padre': data[2]}
        resultados.append(info)
        
        if destino_buscado and data[0] == destino_buscado:
            return info
            
    return resultados


def reconstruir_camino(pila_resultado, origen, destino) -> str:
    """
    Reconstruye el camino visualmente desde una pila de Dijkstra.
    
    Args:
        pila_resultado (Stack): Pila devuelta por dijkstra(origen).
        origen (str): Nombre del nodo origen.
        destino (str): Nombre del nodo destino.
        
    Returns:
        str: Representación en texto del camino (ej. "A -> B -> C").
    """
    # Convertimos la pila a lista para buscar fácil
    datos = obtener_info_dijkstra(pila_resultado) # Esto vacía la pila
    
    # Buscamos el nodo destino en los datos procesados
    nodo_actual = next((x for x in datos if x['nodo'] == destino), None)
    
    if not nodo_actual:
        return f"No hay camino de {origen} a {destino}"
    
    camino = []
    peso_total = nodo_actual['peso']
    
    # Backtracking: Vamos del destino hacia atrás buscando a los padres
    while nodo_actual and nodo_actual['nodo'] != origen:
        camino.append(nodo_actual['nodo'])
        padre = nodo_actual['padre']
        nodo_actual = next((x for x in datos if x['nodo'] == padre), None)
    
    camino.append(origen)
    camino_str = ' -> '.join(reversed(camino))
    costo_str = f"(Costo Total: {peso_total})"
    return f"{color(camino_str, VERDE)} {color(costo_str, AMARILLO)}"


def resolver_ejercicios(grafo: Graph) -> None:
    """
    Ejecuta la lógica para resolver los puntos b, c, d, e, f, g del ejercicio.
    """

    # --- PUNTO B ---
    print(color("\n--- PUNTO B: Barridos (DFS y BFS) ---", NEGRITA + MAGENTA))
    nodos_inicio = ['Red Hat', 'Debian', 'Arch']
    for nodo in nodos_inicio:
        print(f"\n> Barrido desde {color(nodo, CIAN)}:")
        print(color("  DFS (Profundidad):", AMARILLO))
        grafo.deep_sweep(nodo) 
        print(color("  BFS (Amplitud):", AMARILLO))
        grafo.amplitude_sweep(nodo)

    # --- PUNTO C ---
    print(color("\n--- PUNTO C: Camino más corto a Impresora ---", NEGRITA + MAGENTA))
    origenes = ['Manjaro', 'Red Hat', 'Fedora']
    destino = 'Impresora'
    
    for inicio in origenes:
        # Dijkstra devuelve un Stack con todos los caminos desde 'inicio'
        pila_caminos = grafo.dijkstra(inicio)
        ruta = reconstruir_camino(pila_caminos, inicio, destino)
        print(f"Camino {color(inicio, CIAN)} a {color(destino, CIAN)}: {ruta}")

    # --- PUNTO D ---
    print(color("\n--- PUNTO D: Árbol de Expansión Mínima (Kruskal) ---", NEGRITA + MAGENTA))
    # Kruskal devuelve una representación del bosque (árbol) generado
    # Se puede llamar desde cualquier vértice si el grafo es conexo.
    bosque_mst = grafo.kruskal("Manjaro") 
    print("Árbol de expansión mínima generado.")
    # Nota: La implementación de kruskal provista devuelve un string complejo,
    # lo imprimimos tal cual para visualizar la estructura.
    print(bosque_mst)
    
    # --- PUNTO E ---
    print(color("\n--- PUNTO E: Camino más corto a Servidor Guaraní (desde PC, no Notebook) ---", NEGRITA + MAGENTA))
    # Estrategia: Dijkstra DESDE Guaraní hacia todos. Buscamos la PC con menor peso.
    # Como es no dirigido, la distancia Guaraní->PC es igual a PC->Guaraní.
    pila_desde_guarani = grafo.dijkstra('Guaraní')
    todos_los_nodos = obtener_info_dijkstra(pila_desde_guarani)
    
    mejor_pc = None
    menor_distancia = float('inf')
    
    for dato in todos_los_nodos:
        # Buscamos el vértice en el grafo para ver su "other_values" (tipo)
        pos = grafo.search(dato['nodo'], 'value')
        nodo_obj = grafo[pos] # Acceso directo al objeto nodo
        
        if nodo_obj.other_values == 'PC':
            if dato['peso'] < menor_distancia:
                menor_distancia = dato['peso']
                mejor_pc = dato['nodo']
                
    print(f"La PC (no notebook) con el camino más corto a Guaraní es: {color(mejor_pc, VERDE)} (Distancia: {color(menor_distancia, AMARILLO)})")

    # --- PUNTO F ---
    print(color("\n--- PUNTO F: Camino más corto a MongoDB desde equipos del Switch 01 ---", NEGRITA + MAGENTA))
    # 1. Identificar conectados al Switch 1
    pos_switch = grafo.search('Switch 1', 'value')
    conectados_switch1 = []
    for arista in grafo[pos_switch].edges:
        conectados_switch1.append(arista.value) # Nombre del equipo
        
    print(f"Equipos en Switch 1: {color(str(conectados_switch1), AZUL)}")
    
    # 2. Dijkstra desde MongoDB
    pila_desde_mongo = grafo.dijkstra('MongoDB')
    datos_mongo = obtener_info_dijkstra(pila_desde_mongo)
    
    ganador = None
    min_dist_mongo = float('inf')
    
    for equipo in conectados_switch1:
        # Buscar la distancia de este equipo en los resultados de Dijkstra
        info_equipo = next((x for x in datos_mongo if x['nodo'] == equipo), None)
        
        # Filtramos para que sea 'computadora' (PC o Notebook) según el enunciado
        # Aunque en el diagrama conectados al Switch 1 son: Debian (NB), Ubuntu (PC), Mint (PC), Impresora.
        pos_eq = grafo.search(equipo, 'value')
        tipo_eq = grafo[pos_eq].other_values
        
        if info_equipo and tipo_eq in ['PC', 'Notebook']:
            if info_equipo['peso'] < min_dist_mongo:
                min_dist_mongo = info_equipo['peso']
                ganador = equipo
                
    print(f"Computadora del Switch 01 más cercana a MongoDB: {color(ganador, VERDE)} (Distancia: {color(min_dist_mongo, AMARILLO)})")


def punto_g_modificacion(grafo: Graph) -> None:
    """
    Realiza el cambio físico de conexiones y resuelve el punto G.
    """
    print(color("\n--- PUNTO G: Cambio de conexión Impresora ---", NEGRITA + MAGENTA))
    
    # 1. Eliminar conexión Impresora <-> Switch 1
    # Nota: delete_edge devuelve el peso, útil para verificar
    grafo.delete_edge('Impresora', 'Switch 1')
    print(color("Conexión 'Impresora' - 'Switch 1' eliminada.", ROJO))
    
    # 2. Agregar conexión Impresora <-> Router 2
    # Asumiremos un peso arbitrario o el mismo (22) ya que el enunciado no especifica nuevo peso.
    # Usaremos 22 para mantener consistencia, o podrías pedir input.
    grafo.insert_edge('Impresora', 'Router 2', 22)
    print(color("Conexión 'Impresora' - 'Router 2' agregada.", VERDE))
    
    # 3. Volver a resolver punto B
    print(color("\nRepitiendo barridos (Punto B modificado):", AMARILLO))
    grafo.deep_sweep('Red Hat')
    grafo.amplitude_sweep('Red Hat')


# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    # Punto H: Debe utilizar un grafo NO dirigido.
    # Inicializamos con is_directed=False
    red_oficina = Graph(is_directed=False)
    
    # Cargar datos
    cargar_red(red_oficina)
    
    # Resolver lógica
    resolver_ejercicios(red_oficina)
    
    # Modificación final
    punto_g_modificacion(red_oficina)