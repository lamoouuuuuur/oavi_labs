from PIL import Image
import numpy as np


def upsampling(img, m):
    # Get image dimensions
    width, height = img.size
    new_width = int(np.round(width * m))
    new_height = int(np.round(height * m))

    # Create a new empty image
    new_img = Image.new("RGB", size=(new_width, new_height))

    for x in range(new_width):
        for y in range(new_height):
            # Return pixel for coords
            pixel = img.getpixel((int(np.floor(x / m)), int(np.floor(y / m))))

            # Put pixel on coords
            new_img.putpixel((x, y), pixel)

    return new_img


def downsampling(img, n):
    # Get image dimensions
    width, height = img.size
    new_width = int(np.round(width / n))
    new_height = int(np.round(height / n))

    # Create a new empty image
    new_img = Image.new("RGB", size=(new_width, new_height))

    for x in range(new_width):
        for y in range(new_height):
            pixel = img.getpixel((int(np.ceil(x * n)), int(np.ceil(y * n))))
            new_img.putpixel((x, y), pixel)

    return new_img


def resampling_in_one_pass(img, m, n):
    k = m / n

    # Get image dimensions
    width, height = img.size
    new_width = int(round(width * k))
    new_height = int(round(height * k))

    # Create new empty image
    new_img = Image.new("RGB", size=(new_width, new_height))

    for x in range(new_width):
        for y in range(new_height):
            pixel = img.getpixel((x / k, y / k))
            new_img.putpixel((x, y), pixel)

    return new_img
