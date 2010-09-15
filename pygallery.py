import sys
import os
import imghdr
from PIL import Image

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
    if not os.path.isdir(os.path.join(path, "thumbnail")):
        os.mkdir(os.path.join(path, "thumbnail"))
    for f in flist:
        img_path = os.path.join(path, f)
        image = Image.open(img_path)
        thumb_size = 128, 128
        thumbnail = image.thumbnail(thumb_size, Image.ANTIALIAS)
        image.save(os.path.join(path, 'thumbnail', f), "JPEG")

def clean_thumbnail_dir(path):
    if not os.path.isdir(os.path.join(path, "thumbnail")):
        return
    shutil.rmtree(os.path.join(path, "thumbnail"))

def generate_indexhtml(path, flist):
    fhandle = open(os.path.join(path, "index.html"), "w")
    print >> fhandle, "<!DOCTYPE html>"
    print >> fhandle, "<html><body>"
    for f in flist:
        print >> fhandle, "<img src=\"thumbnail/" + f + "\">"
    print >> fhandle, "</body></html>"

def main(params=sys.argv):
    folder = params[1]
    pics = read_folder(folder)
    make_thumbnails(folder, pics)
    generate_indexhtml(folder, pics)
