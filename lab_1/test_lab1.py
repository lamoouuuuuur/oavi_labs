from lab_1.lab_1 import *
import time


def test_upsampling(img, m):
    modified_img = upsampling(img, m)
    modified_img.save("lab_1/modified_images/upsampling_img.png")


def test_downsampling(img, n):
    modified_img = downsampling(img, n)
    modified_img.save("lab_1/modified_images/downsampling_img.png")


def test_two_passes(img, m, n):
    modified_img = downsampling(upsampling(img, m), n)
    modified_img.save("lab_1/modified_images/two_passes.png")


def test_one_pass(img, m, n):
    modified_img = resampling_in_one_pass(img, m, n)
    modified_img.save("lab_1/modified_images/one_passes.png")


