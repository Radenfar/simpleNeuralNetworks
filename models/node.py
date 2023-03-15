class Node:
    def __init__(self):
        self.__children: dict[Node, int] = {}
        self.__value: int = 1

    def set_child(self, child_node, weight: int) -> None:
        self.__children[child_node]= weight
