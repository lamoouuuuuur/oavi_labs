import sys
import os

from PIL import ImageChops, Image

root, dirs, files = list(os.walk("pics/results"))[0]
files.sort()


root_h, dirs_h, files_h = list(os.walk("pics/hists"))[0]
files_h.sort()
#
# _, _, files_i = list(os.walk("inverts_letters"))[0]
# files_i.sort()


with open("Лабораторная работа №6.md", "a") as file:
    img = Image.open(f"pics/reference/string.bmp")
    img = ImageChops.invert(img)
    img.save("pics/reference/text.bmp")

    for i in range(len(files)):
        title = f"{i+1}. \n\n"
        h = f"![](pics/hists/{i}.png)\n\n"
        j = f"![](pics/results/{i}.bmp)\n\n"
        img = Image.open(f"pics/results/{i}.bmp")
        img = ImageChops.invert(img)
        file.writelines([title, j, h])