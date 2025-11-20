
from typing import Any, Optional


class Stack:

    def __init__(self):
        """Inicializa una pila vacía."""
        self.__elements = []


    def push(self, value: Any) -> None:
        """
        Agrega un elemento en la cima de la pila.

        Args:
            value (Any): El elemento a agregar.
        """
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        """
        Elimina y devuelve el elemento de la cima de la pila.

        Returns:
            Optional[Any]: El elemento de la cima, o None si la pila está vacía.
        """
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        """
        Devuelve el número de elementos en la pila.

        Returns:
            int: El tamaño de la pila.
        """
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        """
        Devuelve el elemento de la cima de la pila sin eliminarlo.

        Returns:
            Optional[Any]: El elemento de la cima, o None si la pila está vacía.
        """
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        """
        Muestra todos los elementos de la pila desde la cima hasta la base,
        preservando la pila original.
        """
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())