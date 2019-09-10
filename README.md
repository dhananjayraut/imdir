# imdir

## [PyPI page](https://pypi.org/project/imdir/) [![Actions Status](https://github.com/dhananjayraut/imdir/workflows/Python%20package/badge.svg)](https://github.com/dhananjayraut/imdir/actions)

a simple python package to analyse a directory full of images

## Installation

stable version from pypi

``` bash
pip install imdir
```

### or latest from master branch

```bash
pip install git+https://github.com/dhananjayraut/imdir
```

### Dependencies

* matplotlib
* pillow

## Usage / example

```python
# give path to class
im_dir = image_dir(path="../input/train/",recursive=True, nthreads=4)

imdir.sc_plot(alpha=0.5) # plot height and width as scatter plot

imdir.width_plot() # plot width as histogram using matplotlib

imdir.height_plot() # plot height as histogram using matplotlib
```

## Documentation

```docs
class image_dir(builtins.object)
image_dir(path, recursive=False, nthreads=-1)

image directory class
```

Methods of this class

```docs
__init__(self, path, recursive=False, nthreads=-1)
    Args:
        path (str): path for the directory
        recursive (Boolean): whether to discover all sub directories
                             default False
        nthreads (int): Number of threads used
                        -1 (default) means use all cpu cores
                         0  means do it in main thread (slow)
    Returns:
        a image_dir object
```

```docs
exten_plot(self, **kwds)
    bar plot for the image extensions
    Args:
        **kwds: Additional keyword arguments to
                matplotlib.pyplot 's bar function
```

```docs
height_plot(self, **kwds)
    histogram plot for the image height.
    Args:
        **kwds: Additional keyword arguments to
                matplotlib.pyplot 's hist function
```

```docs
sc_plot(self, **kwds)
    Scatter plot for the image dimensions
    Args:
        **kwds: Additional keyword arguments to
                matplotlib.pyplot 's scatter function
```

```docs
width_plot(self, **kwds)
    histogram plot for the image width.
    Args:
        **kwds: Additional keyword arguments to
                matplotlib.pyplot 's hist function
```

or see help for the image_dir class
```python
help(imdir.image_dir)
```

### Work In progress
