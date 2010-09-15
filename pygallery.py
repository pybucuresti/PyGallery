import sys
import os
import imghdr
from PIL import Image

def main(params=sys.argv):
    return params



def read_folder(path):
    """
    return image files in path
    """
    img_file_list = []
    for f in os.listdir(path):
        img_path = os.path.join(path, f)
        if not os.path.isfile(img_path):
            continue
        if imghdr.what(img_path) is None:
            continue
        img_file_list.append(f)

    return img_file_list

def make_thumbnails(path, flist):
    for f in flist:
        img_path = os.path.join(path, f)
        image = Image.open(img_path)
        thumb_size = 128, 128
        thumbnail = image.thumbnail(thumb_size, Image.ANTIALIAS)
        image.save(os.path.join(path + 'thumbnail', f), "JPEG")
