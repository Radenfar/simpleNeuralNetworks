from models.layer import Layer
from models.node import Node


class Network:
    def __init__(self, depth: int, width: list[int], default_weight: int):
        # setting of attribute vars
        self.__network: list[Layer] = []
        self.__default_weight: int = default_weight
        self.__width: list[int] = width
        self.__size: int = sum(self.__width)
        self.__depth: int = depth

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
    def size(self) -> int:
        return self.__size

    def __str__(self) -> str:
        ret_str: str = ""
        ret_str += f"width: {self.__width}\n"
        ret_str += f"depth: {self.__depth}\n"
        ret_str += f"size: {self.__size}\n"
        return ret_str
