import os
import csv
import random
from models.network import Network
from models.imagehandler import ImageHandler
from models.node import Node
from models.layer import Layer


class Trainer:
    def __init__(self, network: Network, data_path: str, output_path: str, randomness: float, iteration_wait: int = 3):
        self.__network: Network = network  # the network to train
        self.__data_path: str = data_path  # path to the CSV file containing the encoded data
        self.__output_path: str = output_path  # path to the saved resultant image
        self.__randomness: float = randomness  # convert this float into a range for random multiplier of weights
        self.__iteration_wait: int = iteration_wait  # number of iterations to wait before adjusting weights
        self.__iteration: int = 0  # current iteration

    def image_train(self, max_iterations: int = 1000, threshold: float = 0.95):
        """
        Logic:
        - read database into dictionary
        - while current iteration is less or equal to max iterations
            - choose a random image from database dictionary
            - set the input layer node values to the encoded data
            - for each HIDDEN layer:
                - pick a random number of nodes to change based on randomness value
                - for each changing node:
                    - if the current iteration is greater than the last iteration + iteration wait
                        - adjust the weight of a random child by changing the weight by a random multiplier based on self.__randomness
                    - else
                        - pick another node to change until the number of nodes to change are changed
            - for each node in the output layer:
                - group them into RGB tuples by order
            - calculate the similarity score
            - if the score is higher, keep the weights
            - if the score is lower, revert the weights
            - increment the iteration
        - save the image
        """
        encoded_data_dict = self.read_encoded_data()
        previous_score: float = 0.0
        image_handler: ImageHandler = ImageHandler((1024, 1024))
        while self.__iteration <= max_iterations:
            encoded_data = random.choice(list(encoded_data_dict.values()))
            self.__network.set_input_layer(encoded_data)
            self.__network.save_weights()
            for layer_num in range(len(self.__network.hidden_layers)):
                for _ in range(int(self.__randomness * len(self.__network.hidden_layers[layer_num].nodes))):
                    random_choice = random.choice(self.__network.hidden_layers[layer_num].nodes)
                    if self.__iteration > random_choice.last_iteration + self.__iteration_wait:
                        multiplier = (self.__randomness * random.random()) + random.choice([0, 1])
                        random_choice.adjust_random_child(multiplier=multiplier, iteration=self.__iteration)
                    else:
                        continue
            rgb_floats = [node.value for node in self.__network.output_layer.nodes]
            output_rgbs = image_handler.decode(rgb_floats=rgb_floats, path=self.__output_path, save=False)
            input_rgbs = image_handler.decode(rgb_floats=encoded_data, path=self.__output_path, save=False)
            similarity_score = self.image_similarity(output_rgbs, input_rgbs)
            if similarity_score < previous_score:
                self.__network.revert_weights()
            else:
                previous_score = similarity_score
            self.__iteration += 1
        image_handler.decode(rgb_floats=rgb_floats, path=self.__output_path, save=True)

    def encode_data_set(self, encoded_data_path: str):
        """
            Encode a dataset of images and store the encoded data in a CSV file.

            Args:
                encoded_data_path: A string representing the path to the directory containing the images to encode.
                database_path: A string representing the path to the CSV file to store the encoded data.

            Returns:
                A dictionary mapping image filenames to lists of encoded data.
            """
        img_handler = ImageHandler((1024, 1024))
        encoded_data_dict = {}
        for filename in os.listdir(encoded_data_path):
            if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                img_path: str = os.path.join(encoded_data_path, filename)
                encoded_data = img_handler.encode(path=img_path)
                encoded_data_dict[filename] = encoded_data
                with open(self.__data_path, 'a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([filename, encoded_data])
        return encoded_data_dict

    def read_encoded_data(self) -> dict[str, list[float]]:
        encoded_data_dict = {}
        with open(self.__data_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                encoded_data_dict[row[0]] = [float(x) for x in row[1].split(',')]
        return encoded_data_dict

    @staticmethod
    def image_similarity(output_rgbs: list[tuple[int, int, int]], test_data: list[tuple[int, int, int]]) -> float:
        """
        Calculates the Mean Squared Error (MSE) between two lists of RGB values representing images.
        Result of MSE is normalized to a value between 0 and 1.
        """
        mse: float = 0.0
        for i in range(len(output_rgbs)):
            mse += ((output_rgbs[i][0] - test_data[i][0]) ** 2) + ((output_rgbs[i][1] - test_data[i][1]) ** 2) + (
                        (output_rgbs[i][2] - test_data[i][2]) ** 2)
        mse /= len(output_rgbs)
        return (mse / 255 ** 2) / 3
