import os
import PIL
from PIL import Image
from sizes import ANDROID_20DP, ANDROID_LAUNCHER

IMAGE_TYPES = ['png', 'jpg', 'gif']
SOURCE_FOLDER = 'inputs'


def file_type(fname):
    last_dot = fname.rfind('.')
    extension = fname[last_dot+1:] if last_dot >= 0 else None
    return extension


def is_image(fname):
    return file_type(fname) in IMAGE_TYPES


def get_source_files():
    assert os.path.isdir(SOURCE_FOLDER)
    all_files = os.listdir(SOURCE_FOLDER)
    return filter(is_image, all_files)


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

