from typing import Any, Optional

class Queue:

    def __init__(self):
        """Inicializa una cola vacía."""
        self.__elements = []

    def arrive(self, value: Any) -> None:
        """
        Agrega un elemento al final de la cola (enqueue).

        Args:
            value (Any): El elemento a agregar.
        """
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        """
        Elimina y devuelve el elemento del frente de la cola (dequeue).

        Returns:
            Optional[Any]: El elemento del frente, o None si la cola está vacía.
        """
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:
        """
        Devuelve el número de elementos en la cola.

        Returns:
            int: El tamaño de la cola.
        """
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]:
        """
        Devuelve el elemento del frente de la cola sin eliminarlo.

        Returns:
            Optional[Any]: El elemento del frente, o None si la cola está vacía.
        """
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]:
        """
        Mueve el elemento del frente al final de la cola.

        Returns:
            Optional[Any]: El elemento que fue movido, o None si la cola está vacía.
        """
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    
    def show(self):
        """
        Muestra todos los elementos de la cola, preservando su orden original.
        """
        for i in range(len(self.__elements)):
            print(self.move_to_end())
