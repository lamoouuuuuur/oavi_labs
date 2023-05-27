from lab_2.lab_2 import *


def test_semitone(img):
    modified_img = semitone(img)
    modified_img.save("lab_2/modified_images/semitone_cat.bmp")


def test_Niblack(img, k):
    modified_img = Niblack(img, k)
    modified_img.save(f"lab_2/modified_images/niblack_img.png")
