from os import listdir
from os.path import isfile, join
from PIL import Image

IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif',
                  '.tiff', '.webp')


def has_file_allowed_extension(filename, extensions):
    """Checks if a file is an allowed extension.
    Args:
        filename (string): path to a file
        extensions (tuple of strings): extensions to consider (lowercase)
    Returns:
        bool: True if the filename ends with one of given extensions
    """
    return filename.lower().endswith(extensions)


def is_image_file(filename):
    """Checks if a file is an allowed image extension.
    Args:
        filename (string): path to a file
    Returns:
        bool: True if the filename ends with a known image extension
    """
    return has_file_allowed_extension(filename, IMG_EXTENSIONS)


def list_files(path="./"):
    """Returns the list of filepaths for image files in given folder
    Args:
        path (string): path to the folder
    Returns:
       list: list of paths of all image files in that folder
    """
    file_list = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    image_file_list = [f for f in file_list if is_image_file(f)]
    return image_file_list


def get_dimension(image_path):
    """ Gets the dimension of one image
    Args:
        image_path (string): path to the image
    Returns:
       list: list of paths of all image files in that folder
    """
    image = Image.open(image_path)
    return list(image.size)


def get_dimensions(image_path_list):
    """get dimensions of list of images
    Args:
       image_path_list (list): list containing paths of image files
    Returns:
       list: list of paths of all image files in that folder
    """
    return [get_dimension(f) for f in image_path_list]
