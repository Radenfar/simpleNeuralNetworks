from models.layer import Layer
from models.node import Node
from models.network import Network

if __name__ == "__main__":
    DEPTH: int = 4
    NUM_OF_INPUTS: int = int(input("Enter the number of input nodes -: "))
    NUM_OF_OUTPUTS: int = int(input("Enter the number of output nodes -: "))
    WIDTH_HIDDEN: int = int(input("ENter the number of hidden layer nodes -: "))
    WIDTH: list[int] = [NUM_OF_INPUTS] + [WIDTH_HIDDEN]*(DEPTH-2) + [NUM_OF_OUTPUTS]
    DEFAULT_WEIGHT: int = 1
    net: Network = Network(depth=DEPTH, width=WIDTH, default_weight=DEFAULT_WEIGHT)
    print(net)



