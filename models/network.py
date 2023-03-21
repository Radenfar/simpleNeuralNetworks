from models.layer import Layer
from models.node import Node


class Network:
    def __init__(self, depth: int, width: list[int], default_weight: float):
        # setting of attribute vars
        self.__network: list[Layer] = []
        self.__default_weight: float = default_weight
        self.__width: list[int] = width
        self.__size: int = sum(self.__width)
        self.__depth: int = depth
        self.__saved_weights = []

        # create layers
        for x in range(depth):
            new_layer = Layer(number=x, width=width[x], default_weight=default_weight)
            self.__network.append(new_layer)

        # more setting of attr. vars
        self.__input_layer: Layer = self.__network[0]
        self.__output_layer: Layer = self.__network[-1]

        # build weights based on default weight
        for y in range(len(self.__network)):
            if y == (len(self.__network) - 1):
                break
            else:
                for cur_node in self.__network[y].nodes:
                    for next_node in self.__network[y+1].nodes:
                        cur_node.set_child(child_node=next_node, weight=self.__default_weight)
        print(f"Network created with {self.__size} nodes and {self.__depth} layers")

    @property
    def input_layer(self) -> Layer:
        return self.__input_layer

    @property
    def output_layer(self):
        return self.__output_layer

    @property
    def hidden_layers(self) -> list[Layer]:
        return self.__network[0:-1]

    @property
    def network(self) -> list[Layer]:
        return self.__network

    @property
    def size(self) -> int:
        return self.__size

    def set_input_layer(self, new_input_values: list[float]) -> None:
        for i in range(len(self.__input_layer.nodes)):
            self.__input_layer.nodes[i].set_value(new_value=new_input_values[i])
            print(f"Input layer node {i} set to {new_input_values[i]}")

    def forward_propagate(self) -> None:
        for layer in self.hidden_layers:
            for node in layer.nodes:
                node.update_children()

    def save_weights(self) -> None:
        self.__saved_weights = []
        for layer in self.__network:
            current_layer = []
            for node in layer.nodes:
                current_layer.append(node.children)
            self.__saved_weights.append(current_layer)
        print("Weights saved")

    def revert_weights(self) -> None:
        for x in range(len(self.__network)):
            for y in range(len(self.__network[x].nodes)):
                for child in self.__network[x].nodes[y].children:
                    self.__network[x].nodes[y].clear_children()
                    self.__network[x].nodes[y].set_child(child_node=child, weight=self.__saved_weights[x][y][child])
        print("Weights reverted")

    def __str__(self) -> str:
        ret_str: str = ""
        ret_str += f"width: {self.__width}\n"
        ret_str += f"depth: {self.__depth}\n"
        ret_str += f"size: {self.__size}\n"
        return ret_str

