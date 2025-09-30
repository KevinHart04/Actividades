from typing import Any, Optional, List, Tuple

class AVLTree:
    """
    Árbol AVL (BST balanceado) que almacena:
    - value: clave principal usada para ordenar.
    - data: información adicional (diccionario, string, etc.).
    
    Incluye inserción, eliminación, recorridos, búsqueda y utilidades.
    """

    class _Node:
        """Nodo interno del árbol."""
        def __init__(self, value: Any, data: Optional[Any] = None):
            self.value = value
            self.data = data
            self.left: Optional['AVLTree._Node'] = None
            self.right: Optional['AVLTree._Node'] = None
            self.height: int = 0

    def __init__(self):
        self.root: Optional[AVLTree._Node] = None

    # -----------------------------
    # Altura y balance
    # -----------------------------
    def _height(self, node: Optional[_Node]) -> int:
        return -1 if node is None else node.height

    def _update_height(self, node: Optional[_Node]) -> None:
        if node:
            node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _balance_factor(self, node: Optional[_Node]) -> int:
        return 0 if node is None else self._height(node.left) - self._height(node.right)

    # -----------------------------
    # Rotaciones
    # -----------------------------
    def _rotate_right(self, node: _Node) -> _Node:
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_left(self, node: _Node) -> _Node:
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_left_right(self, node: _Node) -> _Node:
        node.left = self._rotate_left(node.left)
        return self._rotate_right(node)

    def _rotate_right_left(self, node: _Node) -> _Node:
        node.right = self._rotate_right(node.right)
        return self._rotate_left(node)

    # -----------------------------
    # Inserción
    # -----------------------------
    def insert(self, value: Any, data: Optional[Any] = None) -> None:
        def _insert(node: Optional[AVLTree._Node], value: Any, data: Optional[Any]) -> AVLTree._Node:
            if node is None:
                return AVLTree._Node(value, data)
            if value < node.value:
                node.left = _insert(node.left, value, data)
            elif value > node.value:
                node.right = _insert(node.right, value, data)
            else:
                node.data = data
                return node

            self._update_height(node)
            balance = self._balance_factor(node)

            if balance > 1 and value < node.left.value:
                return self._rotate_right(node)
            if balance < -1 and value > node.right.value:
                return self._rotate_left(node)
            if balance > 1 and value > node.left.value:
                return self._rotate_left_right(node)
            if balance < -1 and value < node.right.value:
                return self._rotate_right_left(node)

            return node

        self.root = _insert(self.root, value, data)

    # -----------------------------
    # Búsqueda
    # -----------------------------
    def search(self, value: Any) -> Optional[_Node]:
        def _search(node: Optional[AVLTree._Node], value: Any) -> Optional[AVLTree._Node]:
            if node is None:
                return None
            if value == node.value:
                return node
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def proximity_search(self, prefix: str) -> List[Tuple[Any, Any]]:
        """
        Busca todos los nodos cuyo value comienza con el prefijo dado.
        Devuelve lista de (value, data).
        """
        result = []

        def _search(node: Optional[AVLTree._Node]):
            if node:
                if str(node.value).startswith(prefix):
                    result.append((node.value, node.data))
                _search(node.left)
                _search(node.right)

        _search(self.root)
        return result

    # -----------------------------
    # Eliminación
    # -----------------------------
    def delete(self, value: Any) -> Optional[_Node]:
        """
        Elimina un nodo con el valor dado y devuelve el nodo eliminado (si existía).
        """
        deleted_node: Optional[AVLTree._Node] = None

        def _min_value_node(node: AVLTree._Node) -> AVLTree._Node:
            current = node
            while current.left is not None:
                current = current.left
            return current

        def _delete(node: Optional[AVLTree._Node], value: Any) -> Optional[AVLTree._Node]:
            nonlocal deleted_node
            if node is None:
                return None
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                deleted_node = node
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    temp = _min_value_node(node.right)
                    node.value = temp.value
                    node.data = temp.data
                    node.right = _delete(node.right, temp.value)

            self._update_height(node)
            balance = self._balance_factor(node)

            if balance > 1 and self._balance_factor(node.left) >= 0:
                return self._rotate_right(node)
            if balance > 1 and self._balance_factor(node.left) < 0:
                return self._rotate_left_right(node)
            if balance < -1 and self._balance_factor(node.right) <= 0:
                return self._rotate_left(node)
            if balance < -1 and self._balance_factor(node.right) > 0:
                return self._rotate_right_left(node)

            return node

        self.root = _delete(self.root, value)
        return deleted_node

    # -----------------------------
    # Recorridos
    # -----------------------------
    def in_order(self, reverse: bool = False) -> List[Tuple[Any, Any]]:
        def _in_order(node: Optional[AVLTree._Node]):
            if node is None:
                return []
            if reverse:
                return _in_order(node.right) + [(node.value, node.data)] + _in_order(node.left)
            else:
                return _in_order(node.left) + [(node.value, node.data)] + _in_order(node.right)
        return _in_order(self.root)

    def pre_order(self) -> None:
        def _pre_order(node: Optional[AVLTree._Node]):
            if node:
                print(node.value, node.data)
                _pre_order(node.left)
                _pre_order(node.right)
        _pre_order(self.root)

    def post_order(self) -> None:
        def _post_order(node: Optional[AVLTree._Node]):
            if node:
                _post_order(node.left)
                _post_order(node.right)
                print(node.value, node.data)
        _post_order(self.root)

    # -----------------------------
    # Tamaño del árbol
    # -----------------------------
    def size(self) -> int:
        """
        Devuelve la cantidad total de nodos del árbol.
        """
        def _size(node: Optional[AVLTree._Node]) -> int:
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)
