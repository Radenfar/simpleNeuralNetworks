from models.network import Network
from models.imagehandler import ImageHandler
from models.node import Node
from models.layer import Layer

class Trainer:
    def __init__(self, network: Network, data_path: str, output_path: str, randomness: float, iteration_wait: int = 3):
        self.__network: Network = network
        self.__data_path: str = data_path
        self.__output_path: str = output_path
        self.__randomness: float = randomness  # convert this float into a range for random multiplier of weights
        self.__iteration_wait: int = iteration_wait

    def image_train(self, max_iterations: int = 1000):
        ...

    @staticmethod
    def image_similarity(output_rgbs: list[tuple[int, int, int]], test_data: list[tuple[int, int, int]]) -> float:
        """
        Calculates the Mean Squared Error (MSE) between two lists of RGB values representing images.
        Result of MSE is normalized to a value between 0 and 1.
        """
        mse: float = 0.0
        for i in range(len(output_rgbs)):
            mse += ((output_rgbs[i][0] - test_data[i][0]) ** 2) + ((output_rgbs[i][1] - test_data[i][1]) ** 2) + ((output_rgbs[i][2] - test_data[i][2]) ** 2)
        mse /= len(output_rgbs)
        return (mse / 255 ** 2)/3

