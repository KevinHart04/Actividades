from typing import Any, Optional

class List(list):

    CRITERION_FUNCTIONS = {}

    def add_criterion(
        self,
        key_criterion: str,
        function,
    ) -> None:
        """
        Agrega una función de criterio para ordenación y búsqueda.

        Args:
            key_criterion (str): El nombre clave para identificar el criterio.
            function (function): La función lambda o regular que extrae el valor de un objeto.
        """
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(
        self
    ) -> None:
        """Imprime cada elemento de la lista en una nueva línea."""
        for element in self:
            print(element)

    def delete_value(
        self,
        value,
        key_value: str = None,
    ) -> Optional[Any]:
        """
        Busca y elimina un elemento de la lista por su valor.

        Args:
            value (Any): El valor del elemento a eliminar.
            key_value (str, optional): El criterio de búsqueda a utilizar. Defaults to None.

        Returns:
            Optional[Any]: El elemento eliminado, o None si no se encontró.
        """
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    # def insert_value(
    #     self,
    #     value: Any,
    # ) -> None:
    #     # list_number.append(2)
    #     # list_number.insert(1, 11)
    #     pass

    def sort_by_criterion(
        self,
        criterion_key: str = None,
    ) -> None:
        """
        Ordena la lista utilizando un criterio previamente definido.

        Args:
            criterion_key (str, optional): La clave del criterio a usar para la ordenación.
        """
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search(
        self,
        search_value,
        search_key: str = None,
    ) -> Optional[int]:
        """
        Realiza una búsqueda binaria en la lista.

        La lista se ordena primero según el criterio de búsqueda si es necesario.

        Args:
            search_value (Any): El valor que se está buscando.
            search_key (str, optional): La clave del criterio a utilizar para la búsqueda. Defaults to None.

        Returns:
            Optional[int]: El índice del elemento encontrado, o None si no se encuentra.
        """
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value  < search_value:
                start = middle +1
            else:
                end = middle -1
            middle = (start + end) // 2
        return None