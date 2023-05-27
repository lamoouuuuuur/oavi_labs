from lab_3.lab_3 import *


def test_median_filter_hollow(img):
    modified_img = median_filter_hollow(img)
    modified_img.save("lab_3/modified_images/hollow.png")


def test_median_filter_hill(img):
    modified_img = median_filter_hill(img)
    modified_img.save("lab_3/modified_images/hill.png")


def test_difference_hollow(img_1, img_2):
    modified_img = img_difference(img_1, img_2)
    modified_img.save("lab_3/modified_images/difference_hollow.png")


def test_difference_hill(img_1, img_2):
    modified_img = img_difference(img_1, img_2)
    modified_img.save("lab_3/modified_images/difference_hill.png")