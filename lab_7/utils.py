import os

import numpy as np
from PIL import Image, ImageChops

from img_options import mono
from crop_options import cut


s = 'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'

k = 1 / 1.6
white = 255
black = 0


def convert_to_bin(img):
    if str(img.mode) != "1":
        img = mono(img)
    img.save("string.png")
    return img


def get_dif(real, ideal):
    res = 0
    for i in range(len(real)):
        res += (real[i] - ideal[i]) ** 2
    return 1 - res ** 0.5


def attribute(file):
    img = Image.open(file)
    width = img.size[0]
    height = img.size[1]

    weight_black, normal_black, x_center, y_center = 0, 0, 0, 0

    for i in range(width):
        for j in range(height):
            if img.getpixel((i, j)) == black:
                weight_black += 1
                x_center += i
                y_center += j

    size = width * height
    normal_black = weight_black / size

    x_center = x_center / weight_black
    x_norm_center = (x_center - 1) / (width - 1)
    y_center = y_center / weight_black
    y_norm_center = (y_center - 1) / (height - 1)

    x_moment, x_norm_moment, y_moment, y_norm_moment, I45_center, I135_center = (
        0,
        0,
        0,
        0,
        0,
        0,
    )

    for i in range(width):
        for j in range(height):
            if img.getpixel((i, j)) == black:
                x_moment += (j - y_center) ** 2
                y_moment += (i - x_center) ** 2
                I45_center += ((j - y_center - i + x_center) ** 2) / 2
                I135_center += ((j - y_center + i - x_center) ** 2) / 2

    x_norm_moment = x_moment / (weight_black ** 2)
    y_norm_moment = y_moment / (weight_black ** 2)
    I45_rel = I45_center / (weight_black ** 2)
    I135_rel = I135_center / (weight_black ** 2)

    return [
        normal_black,
        x_norm_center,
        y_norm_center,
        x_norm_moment,
        y_norm_moment,
        I135_rel,
        I45_rel,
    ]


reference_letter_close_values = {}
real_letter_close_values = {}

img = Image.open("sentence.png")
img = convert_to_bin(img)

text_len = cut("string.png")

for i in s:
    close = attribute("letters/" + i + ".png")
    reference_letter_close_values[i] = close


for i in range(text_len):
    close = attribute("reference/" + str(i) + ".png")
    real_letter_close_values[i] = close


res = {i: [] for i in range(text_len)}
for i in range(text_len):
    close_letter = real_letter_close_values[i]
    for j in s:
        value = get_dif(close_letter, reference_letter_close_values[j])
        res[i].append({j: value})

    res[i] = sorted(res[i], key=lambda k: list(k.values())[0], reverse=True)

root, dirs, files = list(os.walk("letters"))[0]
files.sort()


root_h, dirs_h, files_h = list(os.walk("reference"))[0]
files_h.sort()


with open("results.md", "a") as file:
    sentence = f"![](sentence.png)\n\n"
    res_sentence = []

    file.writelines(sentence)

    for idx, i in enumerate(s):
        j = f"![](reference/{idx}.png) \n"
        file.writelines(j)

    file.writelines('\n')


    for i in range(len(files_h)):

        j = f"![](reference/{i}.png)\n\n"
        m = reference_letter_close_values[list(res[i][0].keys())[0]]
        dred = ""
        for d in res[i][:5]:
            dred += f"{list(d.keys())[0]} : {list(d.values())[0]}; \n\n"

        file.writelines([j, dred])

    # for i in s:
    #     title = f"{i}  )  \n\n"
    #     j = f"![](letters/{i}.png)\n\n"
    #     file.writelines([title, j])

