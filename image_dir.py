from os import listdir
from os.path import isfile, join
from PIL import Image
import matplotlib.pyplot as plt

IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif',
                  '.tiff', '.webp')


def _has_file_allowed_extension(filename, extensions):
    """Checks if a file is an allowed extension.
    Args:
        filename (string): path to a file
        extensions (tuple of strings): extensions to consider (lowercase)
    Returns:
        bool: True if the filename ends with one of given extensions
    """
    return filename.lower().endswith(extensions)


def _is_image_file(filename):
    """Checks if a file is an allowed image extension.
    Args:
        filename (string): path to a file
    Returns:
        bool: True if the filename ends with a known image extension
    """
    return _has_file_allowed_extension(filename, IMG_EXTENSIONS)


def _list_files(path="./"):
    """Returns the list of filepaths for image files in given folder
    Args:
        path (string): path to the folder
    Returns:
       list: list of paths of all image files in that folder
    """
    file_list = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    image_file_list = [f for f in file_list if _is_image_file(f)]
    return image_file_list


def _get_dimension(image_path):
    """ Gets the dimension of one image
    Args:
        image_path (string): path to the image
    Returns:
       list: list of paths of all image files in that folder
    """
    image = Image.open(image_path)
    return list(image.size)


def _get_dimensions(image_path_list):
    """get dimensions of list of images
    Args:
       image_path_list (list): list containing paths of image files
    Returns:
       list: list of paths of all image files in that folder
    """
    dims = [_get_dimension(f) for f in image_path_list]
    return [f[0] for f in dims], [f[1] for f in dims]


class image_dir:

    def __init__(self, path):
        self.file_list = _list_files(path)
        self.width_list, self.height_list = _get_dimensions(self.file_list)
        return

    def sc_plot(self):
        plt.scatter(self.width_list, self.height_list, alpha=0.5)
        plt.show()

    def width_plot(self):
        plt.hist(self.width_list)
        plt.show()

    def height_plot(self):
        plt.hist(self.height_list)
        plt.show()
