import os, sys
import PIL
from PIL import Image
from sizes import ANDROID_20DP, ANDROID_LAUNCHER, IOS_ICONS

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


def split(fname):
    dot = fname.rfind('.')
    prefix = fname[:dot]
    suffix = fname[dot+1:]
    return prefix, suffix


def resize_one_image(infile_name, sizes=ANDROID_LAUNCHER):
    infile_path = os.path.join(SOURCE_FOLDER, infile_name)
    img = Image.open(infile_path)
    fname, suffix = split(infile_name)
    for (w, h), outfile_path_pattern in sizes:
        outfile_path = outfile_path_pattern.format(fname, suffix)
        print "...saving {}".format(outfile_path)
        out_folder, out_fname = os.path.split(outfile_path)
        if not os.path.exists(out_folder) or not os.path.isdir(out_folder):
            os.mkdir(out_folder)
        resize_and_save(img, w, h, outfile_path)


def __main__(args):
    files = get_source_files()
    for f in files:
        resize_one_image(f, sizes=IOS_ICONS)


if __name__ == "__main__":
    __main__(sys.argv[1:])

