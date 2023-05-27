from lab_4.lab_4 import *


def test_Gx(img):
    modified_image = Gx(img)
    modified_image.save("lab_4/modified_images/Gx.png")


def test_Gy(img):
    modified_image = Gy(img)
    modified_image.save("lab_4/modified_images/Gy.png")


def test_sobel(img, t):
    modified_image = sobel(img, t)
    modified_image.save("lab_4/modified_images/G.png")

