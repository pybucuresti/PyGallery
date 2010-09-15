import sys
import os
import imghdr

def main(params=sys.argv):
    return params



def read_folder(path):
    """
    return image files in path
    """
    img_file_list = []
    for f in os.listdir(path):
        if imghdr.what(os.path.join(path, f)) is None:
            continue
        img_file_list.append(f)

    return img_file_list
