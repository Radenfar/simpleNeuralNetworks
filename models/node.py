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
        """
        - Sets the new_value calculated by the parent node as its current value
        - For each child in self__children:
            - Seperates the childs value from 0.xxxyyyzzz into a list of integers [xxx, yyy, ggg]
            - It then picks a random one of these to be multiplied by the weight
            - Then concatenates the [xxx, yyy, ggg] list back into a single float
            - Sets the chlid's value to this new value
        """
        self.__value = new_value
        for child in self.__children:
            child_value = child.value
            child_value_list = [int(x) for x in str(child_value).split(".")[1:]]
            child_value_list[random.randint(0, len(child_value_list)-1)] *= self.__children[child]
            child_value = float(".".join([str(x) for x in child_value_list]))
            child.set_value(new_value=child_value)
            print(f"Child value set to {child_value}")

    def adjust_random_child(self, multiplier: float, iteration: int) -> None:
        cur_child: Node = random.choice(list(self.__children.keys()))
        print(f"Adjusting child of node by {multiplier} on iteration {iteration}")
        new_weight = self.__children[cur_child] * multiplier
        print(f"New weight: {new_weight}")
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
