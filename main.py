from models.layer import Layer
from models.node import Node
from models.network import Network
from trainer import Trainer

if __name__ == "__main__":
    DATA_PATH = r"C:\Users\adamc\Documents\GitHub_new\simpleNeuralNetworks\images\decoded\dataset.csv"
    OUTPUT_PATH = r"C:\Users\adamc\Documents\GitHub_new\simpleNeuralNetworks"
    DEPTH: int = 4
    NUM_OF_INPUTS: int = int(input("Enter the number of input nodes -: "))
    NUM_OF_OUTPUTS: int = int(input("Enter the number of output nodes -: "))
    WIDTH_HIDDEN: int = int(input("Enter the number of hidden layer nodes -: "))
    WIDTH: list[int] = [NUM_OF_INPUTS] + [WIDTH_HIDDEN]*(DEPTH-2) + [NUM_OF_OUTPUTS]
    DEFAULT_WEIGHT: float = 0.1
    net: Network = Network(depth=DEPTH, width=WIDTH, default_weight=DEFAULT_WEIGHT)
    RANDOMNESS: float = 0.5
    ITERATION_WAIT: int = 3
    trainer: Trainer = Trainer(network=net, data_path=DATA_PATH, output_path=OUTPUT_PATH, randomness=RANDOMNESS, iteration_wait=ITERATION_WAIT)
    trainer.encode_data_set(encoded_data_path=DATA_PATH)
    MAX_ITERATIONS: int = 1000
    THRESHOLD: float = 0.5
    trainer.image_train(max_iterations=MAX_ITERATIONS, threshold=THRESHOLD)


