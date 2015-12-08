import os
import PIL
from PIL import Image
from sizes import ANDROID_20DP


SOURCE_FOLDER = 'inputs'


def get_source_files():
    assert os.path.isdir(SOURCE_FOLDER)
    all_files = os.listdir(SOURCE_FOLDER)
    is_png = lambda name: len(name) >= 5 and name[-4:] == '.png'
    return filter(is_png, all_files)


def resize_and_save(img, w, h, out_fname):
    img = img.resize((w, h), PIL.Image.ANTIALIAS)
    img.save(out_fname)


def resize_one_image(img_fname, sizes):
    img_path = os.path.join(SOURCE_FOLDER, img_fname)
    img = Image.open(img_path)
    for (w, h), out_folder in sizes:
        if not os.path.exists(out_folder) or not os.path.isdir(out_folder):
            os.mkdir(out_folder)
        out_fname = os.path.join(out_folder, img_fname)
        resize_and_save(img, w, h, out_fname)


def __main__():
    files = get_source_files()
    for f in files:
        resize_one_image(f, ANDROID_20DP)


if __name__ == "__main__":
    __main__()

