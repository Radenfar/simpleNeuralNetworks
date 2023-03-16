import random


class Node:
    def __init__(self, parent_layer_number: int):
        self.__parent_layer = parent_layer_number
        self.__children: dict[Node, float] = {}
        self.__value: float = 1.0
        self.__iteration: int = 1

    @property
    def last_iteration(self) -> int:
        return self.__iteration

    @property
    def value(self) -> float:
        return self.__value

    @property
    def children(self):
        return self.__children

    def set_value(self, new_value) -> None:
        self.__value = new_value
        for child in self.__children:
            child.set_value(new_value=new_value * self.__children[child])

    def adjust_random_child(self, multiplier: float, iteration: int) -> None:
        cur_child: Node = random.choice(list(self.__children.keys()))
        new_weight = self.__children[cur_child] * multiplier
        self.set_child(cur_child, new_weight)
        self.__iteration = iteration

    def clear_children(self) -> None:
        self.__children = {}

    def set_child(self, child_node, weight: float) -> None:
        self.__children[child_node] = weight

    def __str__(self):
        ret_str: str = f"Node on layer {self.__parent_layer}\n"
        ret_str += f"Children: {self.__children}\n"
        return ret_str
