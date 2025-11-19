from graph import Graph
from heap import HeapMin
from colores import color, VERDE, AMARILLO, CIAN, MAGENTA, ROJO, NEGRITA, AZUL



def cargar_casa(grafo: Graph) -> None:
    """
    Carga los ambientes (vértices) y las distancias (aristas) cumpliendo las reglas:
    - Mínimo 3 conexiones por nodo.
    - 2 nodos con 5 conexiones (Sala de Estar y Patio).
    """
    ambientes = [
        'Cocina', 'Comedor', 'Cochera', 'Quincho', 
        'Baño 1', 'Baño 2', 'Habitación 1', 'Habitación 2', 
        'Sala de Estar', 'Terraza', 'Patio'
    ]
    
    print(color("--- (A) Cargando Ambientes ---", CIAN))
    for ambiente in ambientes:

        grafo.insert_vertex(ambiente)


    conexiones = [
        # --- Conexiones de la SALA DE ESTAR (5 aristas) ---
        ('Sala de Estar', 'Comedor', 4),
        ('Sala de Estar', 'Cocina', 5),
        ('Sala de Estar', 'Habitación 1', 3), # Dato clave para punto D
        ('Sala de Estar', 'Habitación 2', 4),
        ('Sala de Estar', 'Baño 1', 2),

        # --- Conexiones del PATIO (5 aristas) ---
        ('Patio', 'Quincho', 5),
        ('Patio', 'Cochera', 6),
        ('Patio', 'Terraza', 4),
        ('Patio', 'Cocina', 7), # Doble acceso a cocina
        ('Patio', 'Comedor', 8),

        # --- Rellenando para cumplir mínimo 3 aristas por nodo ---
        
        # Cocina (Ya tiene Sala y Patio) -> Falta 1
        ('Cocina', 'Comedor', 3), 

        # Cochera (Ya tiene Patio) -> Faltan 2
        ('Cochera', 'Quincho', 3),
        ('Cochera', 'Terraza', 10),

        # Quincho (Ya tiene Patio, Cochera) -> Falta 1
        ('Quincho', 'Terraza', 2),

        # Baño 1 (Ya tiene Sala) -> Faltan 2
        ('Baño 1', 'Habitación 1', 2),
        ('Baño 1', 'Habitación 2', 3),

        # Baño 2 (Nuevo, 0 conexiones aun) -> Necesita 3
        ('Baño 2', 'Habitación 2', 2),
        ('Baño 2', 'Terraza', 6),
        ('Baño 2', 'Quincho', 8),

        # Habitación 1 (Tiene Sala, Baño 1) -> Falta 1
        ('Habitación 1', 'Habitación 2', 4),
        
        # Verificamos Habitación 2: Sala, Baño 1, Baño 2, Hab 1 (Tiene 4, OK)
        # Verificamos Terraza: Patio, Cochera, Quincho, Baño 2 (Tiene 4, OK)
        # Verificamos Comedor: Sala, Patio, Cocina (Tiene 3, OK)
    ]

    print(color(f"--- (B) Cargando {len(conexiones)} conexiones (aristas) ---", CIAN))
    for origen, destino, metros in conexiones:
        grafo.insert_edge(origen, destino, metros)


def calcular_metros_mst(grafo: Graph) -> int:
    """
    Calcula el peso total del Árbol de Expansión Mínima (MST).
    
    Nota: El método grafo.kruskal() de la librería devuelve la estructura (el bosque),
    pero no suma los pesos. Esta función auxiliar replica la lógica de selección
    para devolver el número entero requerido en el punto C.
    
    Returns:
        int: Metros totales de cable necesarios.
    """
    bosque = []
    aristas_heap = HeapMin()
    metros_totales = 0

    # Inicializamos el bosque (cada nodo es un árbol separado)
    # y cargamos todas las aristas en el Heap
    for vertice in grafo:
        bosque.append([vertice.value]) # Lista de conjuntos
        for arista in vertice.edges:
            # Guardamos: [peso, origen, destino]
            # Usamos un set o ordenamos string para evitar duplicados en grafos no dirigidos 
            # al sumar, pero Kruskal maneja ciclos, así que el heap estándar sirve.
            aristas_heap.arrive([vertice.value, arista.value], arista.weight)

    # Helper para encontrar en qué árbol está un nodo
    def buscar_en_bosque(val):
        for i, arbol in enumerate(bosque):
            if val in arbol:
                return i
        return -1

    # Algoritmo de Kruskal para sumar pesos
    while len(bosque) > 1 and aristas_heap.size() > 0:
        dato_arista = aristas_heap.attention() # Devuelve [peso, [origen, destino]]
        peso = dato_arista[0]
        origen = dato_arista[1][0]
        destino = dato_arista[1][1]

        idx_origen = buscar_en_bosque(origen)
        idx_destino = buscar_en_bosque(destino)

        if idx_origen != -1 and idx_destino != -1:
            if idx_origen != idx_destino:
                # Si están en árboles distintos, unimos y sumamos peso (cablamos)
                metros_totales += peso
                # Unir los dos árboles en la lista
                arbol_a_mover = bosque.pop(max(idx_origen, idx_destino))
                arbol_base = bosque.pop(min(idx_origen, idx_destino))
                arbol_base.extend(arbol_a_mover)
                bosque.append(arbol_base)
                
    return metros_totales


def resolver_camino_dijkstra(grafo: Graph, origen: str, destino: str):
    """
    Resuelve el punto D usando Dijkstra y reconstruyendo el camino.
    """
    # Ejecutamos Dijkstra desde la Habitación 1
    pila_resultados = grafo.dijkstra(origen)
    
    # Buscamos el destino en la pila
    # La pila trae elementos: [nombre_nodo, peso_acumulado, nombre_padre]
    # Vaciamos la pila en una lista para procesar
    datos = []
    while pila_resultados.size() > 0:
        datos.append(pila_resultados.pop())
    
    # Buscamos el nodo destino (Sala de Estar)
    meta = next((x for x in datos if x[0] == destino), None)
    
    if meta:
        metros = meta[1]
        # Reconstrucción visual del camino (Backtracking)
        camino = [destino]
        padre = meta[2]
        while padre is not None:
            camino.append(padre)
            # Buscar al padre en la lista de datos
            nodo_padre = next((x for x in datos if x[0] == padre), None)
            padre = nodo_padre[2] if nodo_padre else None
            
        ruta_str = ' -> '.join(reversed(camino))
        print(f"Ruta óptima: {color(ruta_str, VERDE)}")
        print(f"Cable necesario para el Smart TV: {color(str(metros), AMARILLO)} metros.")
    else:
        print(color(f"No hay conexión entre {origen} y {destino}.", ROJO))


# --- EJECUCIÓN PRINCIPAL ---

if __name__ == "__main__":
    print(color("=== PROYECTO DOMÓTICA: CABLEADO DE LA CASA ===\n", NEGRITA + AZUL))
    
    # Inicializamos grafo NO dirigido (Punto a: Implementar sobre grafo no dirigido)
    casa = Graph(is_directed=False)
    
    # Puntos A y B: Cargar vértices y aristas
    cargar_casa(casa)

    print(color("\n--- (C) Árbol de Expansión Mínima (Cableado total) ---", NEGRITA + MAGENTA))
    # 1. Mostrar estructura (usando el método original de tu clase)
    estructura_mst = casa.kruskal("Sala de Estar")
    print(color("Estructura del cableado troncal (MST):", AMARILLO))
    print(color(estructura_mst, CIAN))
    
    # 2. Calcular metros (usando nuestra función auxiliar)
    metros_totales = calcular_metros_mst(casa)
    print(f"\n>>> Total de cable para conectar todos los ambientes: {color(str(metros_totales), VERDE + NEGRITA)} metros.")

    print(color("\n--- (D) Conexión Router -> Smart TV ---", NEGRITA + MAGENTA))
    print(color("Buscando camino más corto desde 'Habitación 1' a 'Sala de Estar'...", AMARILLO))
    resolver_camino_dijkstra(casa, "Habitación 1", "Sala de Estar")