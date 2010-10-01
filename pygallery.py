import sys
import os
import imghdr
from PIL import Image
import argparse

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

width = height = 256

def make_thumbnails(path, flist):
    if not os.path.isdir(os.path.join(path, "thumbnail")):
        os.mkdir(os.path.join(path, "thumbnail"))
    for f in flist:
        img_path = os.path.join(path, f)
        image = Image.open(img_path)
        thumb_size = width, height
        thumbnail = image.thumbnail(thumb_size, Image.ANTIALIAS)
        image.save(os.path.join(path, 'thumbnail', f), "JPEG")

def clean_thumbnail_dir(path):
    if not os.path.isdir(os.path.join(path, "thumbnail")):
        return
    shutil.rmtree(os.path.join(path, "thumbnail"))

style_css = """
    body { background-color: black; }
    ul.thumbs { list-style: none; }
    ul.thumbs li { margin: 20px;
                   width: %(width)dpx; height: %(height)dpx;
                   float: left; text-align: center; }
    ul.thumbs li img { padding: 2px; border: 2px solid #333; }
""" % {'width': width, 'height': height}

def generate_indexhtml(path, flist):
    fhandle = open(os.path.join(path, "index.html"), "w")
    print >> fhandle, "<!DOCTYPE html>"
    print >> fhandle, "<html>"
    print >> fhandle, "<head><style>" + style_css + "</style></head>"
    print >> fhandle, "<body><ul class=\"thumbs\">"
    for f in flist:
        print >> fhandle, ("<li><a href=\"" + f + "\">"
                           "<img src=\"thumbnail/" + f + "\">"
                           "</a></li>")
    print >> fhandle, "</ul></body></html>"

def main(params=sys.argv):
    parser = argparse.ArgumentParser(description="Stupid Gallery Generator")
    parser.add_argument('folder', action='store', nargs=1, help='folder storing pictures')
    args = parser.parse_args()
    folder = params[1]
    pics = read_folder(folder)
    make_thumbnails(folder, pics)
    generate_indexhtml(folder, pics)
