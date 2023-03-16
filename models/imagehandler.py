from PIL import Image
import numpy as np


class ImageHandler:
    def __init__(self, desired_resolution: tuple[int, int]):
        self.__desired_resolution = desired_resolution

    def encode(self, path: str) -> list[float]:
        img = Image.open(path)
        img_resized = img.resize(self.__desired_resolution)
        img_array = np.array(img_resized.convert("RGB"))
        # img_array = img_array / 255
        float_list = []
        for r, g, b in img_array.reshape(-1, 3):
            float_val = float(f"0.{r:03d}{g:03d}{b:03d}")
            float_list.append(float_val)
        return float_list

    def decode(self, rgb_floats: list[float], path: str, save: bool) -> None | list[tuple[int, int, int]]:
        rgb_tuples: list[tuple[int, int, int]] = []
        for val in rgb_floats:
            rgb_str = '{:.9f}'.format(val)[2:]
            rgb_str = rgb_str.split('.')[0]
            if not len(rgb_str) == 9:
                rgb_str += '0'
            r, g, b = int(rgb_str[0:3]), int(rgb_str[3:6]), int(rgb_str[6:9])
            rgb_tuples.append((r, g, b))
        if not save:
            return rgb_tuples
        else:
            img = Image.new(mode="RGB", size=self.__desired_resolution)
            img.putdata(rgb_tuples)
            img.save(path)

