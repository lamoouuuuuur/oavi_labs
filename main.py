from lab_1.test_lab1 import *
from lab_2.test_lab2 import *
from lab_3.test_lab3 import *
from lab_4.test_lab4 import *
import time


def lab_1(img, m=3, n=4):
    print(f"M: {m}\n"
          f"N: {n}")
    test_upsampling(img, m)
    test_downsampling(img, n)

    tic_1 = time.perf_counter()
    test_two_passes(img, m, n)
    tac_1 = time.perf_counter()

    tic_2 = time.perf_counter()
    test_one_pass(img, m, n)
    tac_2 = time.perf_counter()

    print(f"test_two_passes: {tac_2 - tic_2:0.4f} sec")
    print(f"test_one_pass: {tac_1 - tic_1:0.4f} sec")


def lab_2(img, k=-0.1):
    test_semitone(img)
    test_Niblack(img, k)


def lab_3(img):
    test_median_filter_hollow(img)
    test_median_filter_hill(img)

    res_1 = Image.open("lab_3/modified_images/hollow.png")
    res_2 = Image.open("lab_3/modified_images/hill.png")

    test_difference_hollow(res_1, img)
    test_difference_hill(res_2, img)


def lab_4(img, t):
    test_Gx(img)
    test_Gy(img)
    test_sobel(img, t)

