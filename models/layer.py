from models.node import Node


class Layer:
    def __init__(self, number: int, width: int, default_weight: float):
        self.__number: int = number
        self.__width: int = width
        self.__nodes: list[Node] = []
        self.__default_weight: float = default_weight
        for i in range(self.__width):
            self.__nodes.append(Node(parent_layer_number=self.__number))

    @property
    def nodes(self) -> list[Node]:
        return self.__nodes

    def add_node(self, new_node: Node) -> None:
        self.__nodes.append(new_node)

    def remove_node(self, a_node) -> None:
        self.__nodes.pop(self.__nodes.index(a_node))
