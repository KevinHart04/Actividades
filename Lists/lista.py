from typing import Any, Optional

class List(list):
    CRITERION_FUNCTIONS = {}

    def add_criterion(self, key_criterion: str, function):
        """Agrega un criterio para ordenar o buscar dentro de la lista"""
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(self):
        """Muestra todos los elementos de la lista"""
        for element in self:
            print(element)

    def delete_value(self, value, key_value: str = None):
        """Elimina un elemento de la lista según un criterio"""
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    def sort_by_criterion(self, criterion_key: str = None):
        """Ordena la lista según un criterio registrado"""
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)
        if criterion is not None:
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print("criterio de orden no encontrado")

    def search(self, search_value, search_key: str = None):
        """Búsqueda binaria de un elemento según un criterio"""
        self.sort_by_criterion(search_key)
        start, end = 0, len(self) - 1

        while start <= end:
            middle = (start + end) // 2
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            else:
                end = middle - 1

        return None
