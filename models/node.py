import random


class Node:
    def __init__(self, parent_layer_number: int):
        self.__parent_layer= parent_layer_number
        self.__children: dict[Node, float] = {}
        self.__value: int = 1
        self.__iteration: int = 1

    @property
    def last_iteration(self) -> int:
        return self.__iteration

    def adjust_random_child(self, multiplier: float) -> None:
        cur_child: Node = random.sample(self.__children.keys(), 1)
        new_weight = self.__children[cur_child] * multiplier
        self.set_child(cur_child, new_weight)

    def set_child(self, child_node, weight: float) -> None:
        self.__children[child_node] = weight

    def __str__(self):
        ret_str: str = f"Node on layer {self.__parent_layer}\n"
        ret_

        return ret_str
