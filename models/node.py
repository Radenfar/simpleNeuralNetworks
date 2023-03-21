import random
import numpy as np

class Node:
    def __init__(self, parent_layer_number: int, connection_count: int):
        self.__parent_layer = parent_layer_number
        self.__children: dict[Node, float] = {}
        self.__value: float = 0.127127127
        self.__iteration: int = 1
        self.__connection_count: int = connection_count

    @property
    def last_iteration(self) -> int:
        return self.__iteration

    @property
    def value(self) -> float:
        return self.__value

    @property
    def children(self):
        return self.__children

    def update_children(self) -> None:
        for child in self.__children:
            value_str = f"{child.value:.9f}"
            print(f"Node {self.__parent_layer} -> {child.__parent_layer} is {value_str}")
            r, g, b = value_str[2:5], value_str[5:8], value_str[8:]
            choice = random.choice(["r", "g", "b"])
            if choice == "r":
                r = self.float_handle(r, child)
            elif choice == "g":
                g = self.float_handle(g, child)
            elif choice == "b":
                b = self.float_handle(b, child)
            new_rgb_value = float(f"0.{r}{g}{b}".rjust(11, "0"))
            print(f"Node {self.__parent_layer} -> {child.__parent_layer} updated to {new_rgb_value:.9f}")
            child.set_value(new_value=new_rgb_value)

    # def change_weight(self, delta: float = 0.1) -> None:
    #     delta_value = random.uniform(-delta, delta)
    #     random_child = random.choice(list(self.__children.keys()))
    #     new_weight = max(0.0001, min(self.__children[random_child] + delta_value, 1.0))
    #     self.__children[random_child] = new_weight

    def change_weight(self, delta: float = 0.1, scale: float = 1.0, iteration: int = 1) -> None:
        delta_value = np.random.uniform(-delta, delta) * scale
        random_child = np.random.choice(list(self.__children.keys()))
        new_weight = max(0.0001, min(self.__children[random_child] + delta_value / iteration, 1.0))
        print(f"New weight for {self.__parent_layer} -> {random_child.__parent_layer} is {new_weight:.9f}")
        self.__children[random_child] = new_weight

    def clear_children(self) -> None:
        self.__children = {}

    def set_value(self, new_value: float) -> None:
        self.__value = new_value

    def set_child(self, child_node, weight: float) -> None:
        # ONLY used in the initialization of the network
        self.__children[child_node] = weight

    def float_handle(self, value: str, child) -> str:
        r_value = int(value) * self.__children[child]
        r_value = max(1, min(r_value, 255))
        r_value = str(r_value).split('.')[0]
        r_value = "0" * (3 - len(r_value)) + r_value
        return r_value

    def __str__(self):
        ret_str: str = f"Node on layer {self.__parent_layer}\n"
        ret_str += f"Children: {self.__children}\n"
        return ret_str


# parent_node: Node = Node(parent_layer_number=1)
# child_node: Node = Node(parent_layer_number=2)
# parent_node.set_child(child_node, 0.5)
# parent_node.set_value(0.255243178)
# for i in range(1):
#     parent_node.change_weight()
#     parent_node.update_children()
#     print(child_node.value)