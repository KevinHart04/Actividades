from typing import Any

class HeapMax:

    def __init__(self):
        """Inicializa un montículo máximo vacío."""
        self.elements = []
    
    def size(self) -> int:
        """
        Devuelve el número de elementos en el montículo.

        Returns:
            int: El tamaño del montículo.
        """
        return len(self.elements)

    def add(self, value: Any) -> None:
        """
        Agrega un elemento al montículo y lo reordena para mantener la propiedad de montículo máximo.

        Args:
            value (Any): El elemento a agregar.
        """
        self.elements.append(value)
        self.float(self.size()-1)
    
    def remove(self) -> Any:
        """
        Elimina y devuelve el elemento de mayor valor (la raíz) del montículo.

        Returns:
            Any: El elemento máximo.
        """
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        """
        Mueve un elemento hacia arriba en el montículo (hacia la raíz) para restaurar
        la propiedad de montículo máximo.

        Args:
            index (int): El índice del elemento a flotar.
        """
        father = (index - 1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            # print(f'flotar desde {index} a {father}')
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        """
        Mueve un elemento hacia abajo en el montículo para restaurar la propiedad
        de montículo máximo.

        Args:
            index (int): El índice del elemento a hundir.
        """
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            mayor = left_son
            if right_son < self.size():
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son

            if self.elements[index] < self.elements[mayor]:
                # print(f'hundir desde {index} a {mayor}')
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False


    def interchange(self, index_1: int, index_2: int) -> None:
        """
        Intercambia dos elementos en la lista interna del montículo.

        Args:
            index_1 (int): Índice del primer elemento.
            index_2 (int): Índice del segundo elemento.
        """
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        """
        Ordena los elementos del montículo en orden descendente.

        Returns:
            list: Una lista con los elementos ordenados.
        """
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        """
        Agrega un elemento con una prioridad asociada. Mayor prioridad significa mayor valor.

        Args:
            value (Any): El valor a almacenar.
            priority (int): La prioridad del valor (ej. 1-bajo, 2-medio, 3-alto).
        """
        self.add([priority, value])
    
    def attention(self) -> Any:
        """
        Atiende (elimina y devuelve) el elemento con la mayor prioridad.

        Returns:
            Any: El elemento con mayor prioridad.
        """
        value = self.remove()
        return value


class HeapMin:

    def __init__(self):
        """Inicializa un montículo mínimo vacío."""
        self.elements = []
    
    def size(self) -> int:
        """
        Devuelve el número de elementos en el montículo.

        Returns:
            int: El tamaño del montículo.
        """
        return len(self.elements)

    def add(self, value: Any) -> None:
        """
        Agrega un elemento al montículo y lo reordena para mantener la propiedad de montículo mínimo.

        Args:
            value (Any): El elemento a agregar.
        """
        self.elements.append(value)
        self.float(self.size()-1)
    
    def search(self, value):
        """
        Busca un valor dentro del montículo.

        Nota: Esta es una búsqueda lineal (O(n)), no aprovecha la estructura del montículo.

        Args:
            value (Any): El valor a buscar en la segunda posición de los elementos internos.

        Returns:
            int or None: El índice del elemento si se encuentra, de lo contrario None.
        """
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index

    def remove(self) -> Any:
        """
        Elimina y devuelve el elemento de menor valor (la raíz) del montículo.

        Returns:
            Any: El elemento mínimo.
        """
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        """
        Mueve un elemento hacia arriba en el montículo (hacia la raíz) para restaurar
        la propiedad de montículo mínimo.

        Args:
            index (int): El índice del elemento a flotar.
        """
        father = (index - 1) // 2
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        """
        Mueve un elemento hacia abajo en el montículo para restaurar la propiedad
        de montículo mínimo.

        Args:
            index (int): El índice del elemento a hundir.
        """
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            minor = left_son
            if right_son < self.size():
                if self.elements[right_son] < self.elements[minor]:
                    minor = right_son

            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False


    def interchange(self, index_1: int, index_2: int) -> None:
        """
        Intercambia dos elementos en la lista interna del montículo.

        Args:
            index_1 (int): Índice del primer elemento.
            index_2 (int): Índice del segundo elemento.
        """
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # def monticulizar

    def heapsort(self) -> list:
        """
        Ordena los elementos del montículo en orden ascendente.

        Returns:
            list: Una lista con los elementos ordenados.
        """
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        """
        Agrega un elemento con una prioridad asociada. Menor prioridad significa mayor importancia.

        Args:
            value (Any): El valor a almacenar.
            priority (int): La prioridad del valor.
        """
        self.add([priority, value])
    
    def attention(self) -> Any:
        """
        Atiende (elimina y devuelve) el elemento con la menor prioridad (el más importante).

        Returns:
            Any: El elemento con menor prioridad.
        """
        value = self.remove()
        return value

    def change_priority(self, index, new_priority):
        """
        Cambia la prioridad de un elemento existente en el montículo y lo reordena.

        Args:
            index (int): El índice del elemento cuya prioridad se va a cambiar.
            new_priority (int): El nuevo valor de la prioridad.
        """
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.sink(index)
            elif new_priority < previous_priority:
                self.float(index)
