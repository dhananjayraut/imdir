import os
from PIL import Image
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt

_IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif',
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
    return _has_file_allowed_extension(filename, _IMG_EXTENSIONS)


def _list_files(path="./", recursive=False):
    """Returns the list of filepaths for image files in given folder
    Args:
        path (string): path to the folder
        recursive (Boolean): whether to discover all sub directories
    Returns:
       list: list of paths of all image files in that folder
    """
    if recursive is False:
        file_list = [os.path.join(path, f) for f in os.listdir(path)
                     if os.path.isfile(os.path.join(path, f))]
    else:
        file_list = []
        for folder, subs, files in os.walk(path):
            for filename in files:
                file_list.append(os.path.join(folder, filename))
    image_file_list = [f for f in file_list if _is_image_file(f)]
    return image_file_list


def _get_dimension(image_path):
    """ Gets the dimension of one image
    Args:
        image_path (string): path to the image
    Returns:
       list: list of paths of all image files in that folder
    """
    width, height = -1, -1
    try:
        width, height = list(Image.open(image_path).size)
    except:
        print("Error Ocured with file " + image_path)
    finally:
        return [width, height]


def _get_dimensions(image_path_list, nthreads=-1):
    """get dimensions of list of images
    Args:
       image_path_list (list): list containing paths of image files
    Returns:
       list: list of paths of all image files in that folder
    Note:- Returns -1, -1 for corrupt files.
    """

    if nthreads == 0:
        dims = [_get_dimension(f) for f in image_path_list]
    else:
        if nthreads == -1:
            nthreads = cpu_count()
        with Pool(nthreads) as p:
            dims = p.map(_get_dimension, image_path_list)
    return [f[0] for f in dims], [f[1] for f in dims]


def _get_extensions(image_path_list):
    """get extensions of list of images
    Args:
       image_path_list (list): list containing paths of image files
    Returns:
       list: list of extensions of all image files in that folder
    """
    return [str(f).split('.')[-1] for f in image_path_list]


def _correct_them(fl, wl, hl):
    """Checks for corrupt files using dimensions
    Args:
        fl (list): list containing paths of image files
        wl (list): list containing width of image files
        hl (list): list containing heights of image files
    Returns:
       list: list of extensions of all image files in that folder
    """
    file_list, corrupt_list = [], []
    width_list, height_list = [], []

    for i, width in enumerate(wl):
        if width == -1:
            corrupt_list.append(fl[i])
        else:
            width_list.append(wl[i])
            height_list.append(hl[i])
            file_list.append(fl[i])

    return file_list, corrupt_list, width_list, height_list


class image_dir:
    """
    image directory class
    """
    def __init__(self, path, recursive=False, nthreads=-1):
        """
        Args:
            path (str): path for the directory
            recursive (Boolean): whether to discover all sub directories
                                 default False
            nthreads (int): Number of Processes to use
                            -1 (default) means use all cpu cores
                            0  means do it in main thread (slow)
        Returns:
            a image_dir object
        """
        filelist = _list_files(path, recursive)
        widthlist, heightlist = _get_dimensions(filelist, nthreads)
        fl, cl, wl, hl = _correct_them(filelist, widthlist, heightlist)
        self.file_list, self.corrupt_file_list = fl, cl
        self.width_list, self.height_list = wl, hl
        exten_list = _get_extensions(self.file_list)
        exts = list(set(set(exten_list)))
        self.exten_counts = {str(i): exten_list.count(i) for i in exts}
        return

    def sc_plot(self, **kwds):
        """
        Scatter plot for the image dimensions
        Args:
            **kwds: Additional keyword arguments to
                    matplotlib.pyplot 's scatter function
        """
        plt.scatter(self.width_list, self.height_list, **kwds)
        plt.show()

    def width_plot(self, **kwds):
        """
        histogram plot for the image width.
        Args:
            **kwds: Additional keyword arguments to
                    matplotlib.pyplot 's hist function
        """
        plt.hist(self.width_list, **kwds)
        plt.show()

    def height_plot(self, **kwds):
        """
        histogram plot for the image height.
        Args:
            **kwds: Additional keyword arguments to
                    matplotlib.pyplot 's hist function
        """
        plt.hist(self.height_list, **kwds)
        plt.show()

    def exten_plot(self, **kwds):
        """
        bar plot for the image extensions
        Args:
            **kwds: Additional keyword arguments to
                    matplotlib.pyplot 's bar function
        """
        exts = list(self.exten_counts.keys())
        counts = list(self.exten_counts.values())
        plt.bar(exts, counts, **kwds)
        plt.show()
