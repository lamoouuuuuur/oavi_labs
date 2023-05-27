from PIL import Image, ImageDraw
import math
import numpy as np
from math import sqrt


def semitone(img):
    width, height = img.size
    new_img = Image.new("L", size=(width, height))
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            gray = 0.3 * pixel[0] + 0.59 * pixel[1] + 0.11 * pixel[2]
            new_img.putpixel((x, y), int(gray))
    return new_img


def Niblack(img, k):
    imageIn = np.array(semitone(img))
    # Create new image with same characteristics(height + width), white color
    imageNew = np.zeros(imageIn.shape) + 255

    # Size of window
    w = 15

    for i in range(w + 1, len(imageIn) - w):
        for j in range(w + 1, len(imageIn[i]) - w):
            imageFormed = []

            # Extract the window to calculate the threshold for each window

            for x in range(len(imageIn[i - w: i + w])):
                # Forming new image with window size
                imageFormed.append(imageNew[i-w:i+w][x][j-w:j+w])
            mean = np.asarray(imageFormed).mean()
            stdev = np.asarray(imageFormed).std()
            T = mean + k * stdev

            # Compare pixels
            if imageIn[i][j] < T:
                imageNew[i][j] = 0
            else:
                imageNew[i][j] = 255

    imageNew = imageNew.astype(np.uint8)
    result_img = Image.fromarray(imageNew)
    return result_img





















