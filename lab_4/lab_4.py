from PIL import Image, ImageChops
import numpy as np


def semitone(img):
    width, height = img.size
    new_img = Image.new("L", size=(width, height))
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            gray = 0.3 * pixel[0] + 0.59 * pixel[1] + 0.11 * pixel[2]
            new_img.putpixel((x, y), int(gray))
    return new_img


def Gx(img):
    if str(img.mode) != "L":
        img = semitone(img)
        img.save("lab_4/modified_images/semitone.png")
    width, height = img.size
    new_image = Image.new("L", size=(width, height))
    for x in range(width)[1:-2]:
        for y in range(height)[1:-2]:
            z1 = img.getpixel((x - 1, y - 1))
            z2 = img.getpixel((x, y - 1))
            z3 = img.getpixel((x + 1, y - 1))
            z7 = img.getpixel((x - 1, y + 1))
            z8 = img.getpixel((x, y + 1))
            z9 = img.getpixel((x + 1, y + 1))

            Gx = z7 + 2 * z8 + z9 - (z1 + 2 * z2 + z3)

            new_image.putpixel((x, y), Gx)

    return new_image


def Gy(img):
    if str(img.mode) != "L":
        img = semitone(img)
        img.save("lab_4/modified_images/semitone.png")
    width, height = img.size
    new_image = Image.new("L", size=(width, height))
    for x in range(width)[1:-2]:
        for y in range(height)[1:-2]:
            z1 = img.getpixel((x - 1, y - 1))
            z3 = img.getpixel((x + 1, y - 1))
            z4 = img.getpixel((x - 1, y))
            z6 = img.getpixel((x + 1, y))
            z7 = img.getpixel((x - 1, y + 1))
            z9 = img.getpixel((x + 1, y + 1))

            Gy = z3 + 2*z6 + z9 - (z1 + 2*z4 + z7)

            new_image.putpixel((x, y), Gy)

    return new_image


def sobel(img, t):
    if str(img.mode) != "L":
        img = semitone(img)
        img.save("lab_4/modified_images/semitone.png")

    width, height = img.size

    new_image = Image.new("L", size=(width, height))

    df_max = 0

    for x in range(width)[1:-2]:
        for y in range(height)[1:-2]:
            z1 = img.getpixel((x - 1, y - 1))
            z2 = img.getpixel((x, y - 1))
            z3 = img.getpixel((x + 1, y - 1))
            z4 = img.getpixel((x - 1, y))
            z5 = img.getpixel((x, y))
            z6 = img.getpixel((x + 1, y))
            z7 = img.getpixel((x - 1, y + 1))
            z8 = img.getpixel((x, y + 1))
            z9 = img.getpixel((x + 1, y + 1))

            Gx = z7 + 2*z8 + z9 - (z1 + 2*z2 + z3)
            Gy = z3 + 2*z6 + z9 - (z1 + 2*z4 + z7)
            df = abs(Gx) + abs(Gy)

            if df > df_max:
                df_max = df

    df_max = 255 / df_max

    for x in range(width)[1:-2]:
        for y in range(height)[1:-2]:
            z1 = img.getpixel((x - 1, y - 1))
            z2 = img.getpixel((x, y - 1))
            z3 = img.getpixel((x + 1, y - 1))
            z4 = img.getpixel((x - 1, y))
            z5 = img.getpixel((x, y))
            z6 = img.getpixel((x + 1, y))
            z7 = img.getpixel((x - 1, y + 1))
            z8 = img.getpixel((x, y + 1))
            z9 = img.getpixel((x + 1, y + 1))

            Gx = z7 + 2 * z8 + z9 - (z1 + 2 * z2 + z3)
            Gy = z3 + 2 * z6 + z9 - (z1 + 2 * z4 + z7)
            df = abs(Gx) + abs(Gy)
            df_norm = df * df_max

            if df_norm > t:
                new_image.putpixel((x, y), 255)
            else:
                new_image.putpixel((x, y), 0)

    return new_image








