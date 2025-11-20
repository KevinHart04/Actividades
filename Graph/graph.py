from typing import Any, Optional

from heap import HeapMin
from list_ import List
from queue_ import Queue
from stack import Stack

class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            """
            Inicializa un nodo de vértice.

            Args:
                value (Any): El valor principal del vértice.
                other_values (Optional[Any], optional): Otros valores asociados al vértice. Defaults to None.
            """
            self.value = value
            self.edges = List()
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            self.visited = False
        
        def __str__(self):
            """Devuelve la representación en cadena del valor del vértice."""
            return self.value
    
    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            """
            Inicializa un nodo de arista.

            Args:
                value (Any): El vértice de destino de la arista.
                weight (Any): El peso de la arista.
                other_values (Optional[Any], optional): Otros valores asociados a la arista. Defaults to None.
            """
            self.value = value
            self.weight = weight
            self.other_values = other_values # no esta en uso aun
        
        def __str__(self):
            """Devuelve la representación en cadena de la arista."""
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    def __init__(self, is_directed=False):
        """
        Inicializa el grafo.

        Args:
            is_directed (bool, optional): Indica si el grafo es dirigido. Defaults to False.
        """
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def _order_by_value(item):
        """Criterio de ordenación para nodos basado en su valor principal."""
        return item.value

    def _order_by_weight(item):
        """Criterio de ordenación para aristas basado en su peso."""
        return item.weight
    
    def show(
        self
    ) -> None:
        """
        Muestra la estructura del grafo en la consola.
        
        Itera sobre cada vértice y muestra su valor, seguido de todas sus aristas
        y los pesos correspondientes.
        """
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show() 

    def insert_vertex(self, value: Any, other_values: Any = None) -> None:
            """
            Inserta un vértice en el grafo.
            
            Args:
                value (Any): Valor principal del vértice (ej. nombre del equipo).
                other_values (Any, optional): Datos adicionales (ej. tipo: PC, Switch).
            """
            node_vertex = Graph.__nodeVertex(value, other_values) 
            self.append(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
            """
            Inserta una arista entre dos vértices. Maneja la bidireccionalidad.
            """
            origin = self.search(origin_vertex, 'value')
            destination = self.search(destination_vertex, 'value')
            if origin is not None and destination is not None:
                node_edge = Graph.__nodeEdge(destination_vertex, weight)
                self[origin].edges.append(node_edge)
                
                if not self.is_directed and origin != destination: 
                    node_edge = Graph.__nodeEdge(origin_vertex, weight)
                    self[destination].edges.append(node_edge)
            else:
                print(f'Error: No se pudo unir {origin_vertex} con {destination_vertex}. Faltan vértices.')

    def delete_edge(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        """
        Elimina una arista entre dos vértices.

        Si el grafo no es dirigido, elimina también la arista en la dirección opuesta.

        Args:
            origin (Any): El valor del vértice de origen.
            destination (Any): El valor del vértice de destino.
            key_value (str, optional): La clave para buscar los vértices. Defaults to None.

        Returns:
            Optional[Any]: La arista eliminada o None si no se encontró.
        """
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            if self.is_directed and edge is not None:
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        """
        Elimina un vértice del grafo y todas las aristas asociadas a él.

        Args:
            value (Any): El valor del vértice a eliminar.
            key_value_vertex (str, optional): La clave para buscar el vértice. Defaults to None.
            key_value_edges (str, optional): La clave para buscar las aristas a eliminar. 
                                             Defaults to 'value'.

        Returns:
            Optional[Any]: El vértice eliminado o None si no se encontró.
        """
        delete_value = self.delete_value(value, key_value_vertex)
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    def mark_as_unvisited(self) -> None:
        """Marca todos los vértices del grafo como no visitados."""
        for vertex in self:
            vertex.visited = False

    def exist_path(self, origin, destination):
        """
        Verifica si existe un camino entre dos vértices.

        Args:
            origin (Any): El valor del vértice de origen.
            destination (Any): El valor del vértice de destino.

        Returns:
            bool: True si existe un camino, False en caso contrario.
        """
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.value, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result
        
        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result
    
    def deep_sweep(self, value) -> None:
        """
        Realiza un barrido en profundidad (DFS) del grafo desde un vértice de inicio.
        Imprime los vértices a medida que los visita.

        Args:
            value (Any): El valor del vértice desde el que se inicia el barrido.
        """
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.search(edge.value, 'value')
                        if not graph[destination_edge_pos].visited:
                            __deep_sweep(graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)
        
    def amplitude_sweep(self, value)-> None:
        """
        Realiza un barrido en amplitud (BFS) del grafo desde un vértice de inicio.
        Imprime los vértices a medida que los visita.

        Args:
            value (Any): El valor del vértice desde el que se inicia el barrido.
        """
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                queue_vertex.arrive(self[vertex_pos])
                while queue_vertex.size() > 0:
                    vertex = queue_vertex.attention()
                    print(vertex.value)
                    for edge in vertex.edges:
                        destination_edge_pos = self.search(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                queue_vertex.arrive(self[destination_edge_pos])

    def dijkstra(self, origin):
        """
        Calcula el camino más corto desde un vértice de origen a todos los demás
        vértices del grafo utilizando el algoritmo de Dijkstra.

        Args:
            origin (Any): El valor del vértice de origen.

        Returns:
            Stack: Una pila que contiene los resultados. Cada elemento de la pila es una
                   lista con la forma [vértice, costo_total, vértice_padre], representando
                   el camino más corto desde el origen.
        """
        from math import inf
        no_visited = HeapMin()
        path = Stack()
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)
        while no_visited.size() > 0:
            value = no_visited.attention()
            costo_nodo_actual = value[0]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges
            for edge in edges:
                pos = no_visited.search(edge.value)
                if pos is not None:
                    if pos is not None:
                        if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                            no_visited.elements[pos][1][2] = value[1][0]
                            no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path

    def kruskal(self, origin_vertex):
        """
        Encuentra el Árbol de Expansión Mínima (MST) del grafo utilizando el algoritmo de Kruskal.

        Args:
            origin_vertex (Any): Un vértice de referencia para determinar a qué árbol
                                 pertenece el resultado final en caso de un grafo no conexo.

        Returns:
            str or list: Una representación en cadena del árbol de expansión mínima que
                         contiene al `origin_vertex`. Si el grafo es no conexo, puede devolver
                         una lista de los árboles (bosque). La representación en cadena
                         describe las aristas que forman el MST.
        """
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
                
        forest = []
        edges = HeapMin()
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.value], edge.weight)
        
        while len(forest) > 1 and edges.size() > 0:
            edge = edges.attention()
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])
            if origin is not None and destination is not None:
                if origin != destination:
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)


                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')
        
        from_vertex = search_in_forest(forest, origin_vertex)
        
        return forest[from_vertex] if from_vertex is not None else forest
