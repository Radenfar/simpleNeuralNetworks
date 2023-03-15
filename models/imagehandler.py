from PIL import Image
import numpy as np
from typing import Union


class ImageHandler:
    def __init__(self, desired_resolution: tuple[int, int]):
        self.__desired_resolution = desired_resolution

    def encode(self, path: str) -> list[float]:
        img = Image.open(path)
        img_resized = img.resize(self.__desired_resolution)
        img_array = np.array(img_resized.convert("RGB"))
        float_list = []
        for r, g, b in img_array.reshape(-1, 3):
            float_val = float(f"0.{r:03d}{g:03d}{b:03d}")
            float_list.append(float_val)
        return float_list

    def decode(self, rgb_floats: list[float], path: str) -> None:
        rgb_array = np.array(
            [[(int(val * 1000) // 1000000) % 10, (int(val * 1000) // 1000) % 1000, int(val * 1000) % 1000] for val in
             rgb_floats], dtype=np.uint8)
        rgb_array = rgb_array.reshape(self.__desired_resolution[1], self.__desired_resolution[0], 3)
        img = Image.fromarray(rgb_array)
        img.save(path)
