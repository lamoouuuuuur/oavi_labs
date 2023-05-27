from PIL import Image, ImageChops
import numpy as np


def median_filter_hollow(img):
    core = np.array([[0, 0, 1, 0, 0],
                    [0, 1, 1, 1, 0],
                    [1, 1,  1, 1, 1],
                    [0, 1, 1, 1, 0],
                    [0, 0, 1, 0, 0]])

    border = np.sum(core) / 2
    pixies = np.array(img)

    if 255 in pixies:
        pixies = np.divide(pixies, 255)

    size = 5
    pixies_value = np.zeros((5, 5))
    median = int((size - 1) / 2)

    for i in range(median, pixies.shape[0] - median):
        for j in range(median, pixies.shape[1] - median):
            for k in range(size):
                for l in range(size):
                    pixies_value[k, l] = pixies[i - median + k, j - median + l]

            sum = np.sum(pixies_value * core)

            if sum > border:
                pixies[i, j] = 1
            else:
                pixies[i, j] = 0

    pixies = pixies * 255
    new_img = Image.fromarray(pixies.astype(np.uint8))

    return new_img


def median_filter_hill(img):
    core = np.array([[1, 1, 1, 1, 1],
                     [1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1],
                     [1, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1]])

    border = np.sum(core) / 2
    pixies = np.array(img)

    if 255 in pixies:
        pixies = np.divide(pixies, 255)

    size = 5
    pixies_value = np.zeros((5, 5))
    median = int((size - 1) / 2)

    for i in range(median, pixies.shape[0] - median):
        for j in range(median, pixies.shape[1] - median):
            for k in range(size):
                for l in range(size):
                    pixies_value[k, l] = pixies[i - median + k, j - median + l]

            sum = np.sum(pixies_value * core)
            if sum > border:
                pixies[i, j] = 1
            else:
                pixies[i, j] = 0

    pixies = pixies * 255
    new_img = Image.fromarray(pixies.astype(np.uint8))

    return new_img


def img_difference(img_1, img_2):
    diff = ImageChops.difference(img_1, img_2)
    result = ImageChops.invert(diff)
    return result

