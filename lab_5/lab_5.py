import pandas as pd

from utils import gen_letters_reference_images
from utils import get_hist_profile
from utils import generate_csv
import warnings

warnings.filterwarnings("ignore")

s = 'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'


def main():
    gen_letters_reference_images(s)
    gen_letters_reference_images(s, True)
    get_hist_profile(s)
    get_hist_profile(s)
    generate_csv(s)


if __name__ == "__main__":
    main()
