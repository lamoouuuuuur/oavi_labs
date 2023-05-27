from PIL import Image, ImageDraw
from clint.textui import progress
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)


def create_apply_func(d=1, phi=(0,)):
    def apply_func(img, pix, pos):
        res = np.zeros(WHITE[0]+1)
        pixs = img.load()
        base_x, base_y = pos
        for angle in phi:
            x = base_x + np.around(np.cos(angle/180*np.pi))*d
            y = base_y + np.around(np.sin(angle/180*np.pi))*d
            if 0 <= x < img.size[0] and 0 <= y < img.size[1]:
                val = pix[x, y][0]
                res[val] += 1
        return (pix[base_x, base_y][0], res)
    return apply_func


def pixel_gen(img, apply_func=lambda img, pix, x: pix[x]):
    pix = img.load()
    for row in range(img.size[1]):
        for col in range(img.size[0]):
            pos = (col, row)
            yield pos, apply_func(img, pix, pos)


def Haralic_matrix(name, mono_img, d, phi):
    res = np.zeros((WHITE[0] + 1, WHITE[0] + 1))
    hist = np.zeros(WHITE[0] + 1)
    func = create_apply_func(d=d, phi=phi)
    max_max = 0
    for pos, (val, row) in progress.bar(pixel_gen(mono_img, func), expected_size=mono_img.size[0] * mono_img.size[1]):
        res[val] += row
        max_max = max(max_max, max(row))
        hist[val] += 1
    res_img = Image.fromarray(np.uint8(res * 255 / max_max))
    res_img.save(f"{name}_matrix.jpg", "JPEG")
    return res_img, hist


def calc_params(h_img, hist):
    res_s = pd.Series({"asm": 0, "mpr": 0, "ent": 0, "tr": 0})
    max_i, max_j = [0, 0], [0, 0]
    for idx, p in enumerate(hist):
        if p > max_j[1]:
            max_i = max_j.copy()
            max_j = [idx, p]
        elif p > max_i[1]:
            max_i = [idx, p]
    for (i, j), p in progress.bar(pixel_gen(h_img), expected_size=h_img.size[0] * h_img.size[1]):
        res_s["asm"] += p ** 2
        if i == max_i[0] and j == max_j[0]:
            res_s["mpr"] = p
        if p != 0:
            res_s["ent"] -= p * np.log2(p)
        if i == j:
            res_s["tr"] += p
    return res_s


def histogram_equalization(image):
    image_array = np.array(image)
    hist, bins = np.histogram(image_array.flatten(), bins=256, range=(0, 256))
    hist_norm = hist.cumsum() / hist.sum()
    equalized_image = np.interp(image_array.flatten(), bins[:-1], hist_norm * 255)
    equalized_image = equalized_image.reshape(image_array.shape).astype(np.uint8)
    equalized_image_pil = Image.fromarray(equalized_image)
    return equalized_image_pil


methods = (
    ("hist", histogram_equalization),
)

file_name = "wallWall.png"


def main():
    name = file_name.split('.')[0]
    mono_img = Image.open(file_name)
    draw = ImageDraw.Draw(mono_img)
    for pos, p in pixel_gen(mono_img):
        s = sum(p[:3]) // 3
        draw.point(pos, (s, s, s))
    mono_img.save(f"mono_{name}.jpg", "JPEG")

    haralic_param = (
        (1, (0, 90, 180, 270)),
    )
    for idx, (d, phi) in enumerate(haralic_param):
        directory = f"pics_{idx}"
        if not os.path.exists(directory):
            os.makedirs(directory)

        new_name = f"{directory}/{name}_{idx}"
        tmp_img, hist = Haralic_matrix(new_name, mono_img, d, phi)
        f = plt.figure()
        plt.bar(np.arange(hist.size), hist)
        plt.savefig(f"{new_name}_bar.png")
        plt.close(f)
        calc_params(tmp_img, hist).to_csv(f"{new_name}.csv", header=True)

        for m_idx, (m_name, method) in enumerate(methods):
            new_new_name = f"{new_name}_{m_idx}_{m_name}"
            new_img = method(mono_img)

            new_img.save(f"{new_new_name}.jpg", "JPEG")
            new_tmp_img, new_hist = Haralic_matrix(new_new_name, new_img, d, phi)
            f = plt.figure()
            plt.bar(np.arange(new_hist.size), new_hist)
            plt.savefig(f"{new_new_name}_bar.png")
            plt.close(f)
            calc_params(new_tmp_img, new_hist).to_csv(f"{new_new_name}.csv", header=True)


if __name__ == "__main__":
    main()