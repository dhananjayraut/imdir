# imdir

[![Actions Status](https://github.com/dhananjayraut/imdir/workflows/Python%20package/badge.svg)](https://github.com/dhananjayraut/imdir/actions) [![PyPI version](https://badge.fury.io/py/imdir.svg)](https://pypi.org/project/imdir/) [![Python 3.6](https://img.shields.io/pypi/pyversions/imdir.svg)](https://pypi.org/project/imdir/)

a simple python package to analyse a directory full of images

## Features

- Easy Interface to remember
- Analyse distribution of height, width, extensions etc.
- Multithreaded for faster execution
- high customizability for plots
- Detects corupt files
- well tested on diffrent platforms

## Installation

stable version from pypi [page](https://pypi.org/project/imdir/)

``` bash
pip install imdir
```

### or latest from master branch

```bash
pip install git+https://github.com/dhananjayraut/imdir
```

### Dependencies

- matplotlib
- pillow

## Usage / example

```python
from imdir import image_dir
# give path to class
im_dir = image_dir(path="../input/train/",recursive=True, nthreads=4)

im_dir.sc_plot(alpha=0.5) # plot height and width as scatter plot

im_dir.width_plot() # plot width as histogram using matplotlib

im_dir.height_plot() # plot height as histogram using matplotlib
```

## Documentation

[Generated documentation](https://dhananjayraut.github.io/imdir/)

or see help for the image_dir class

```python
help(imdir.image_dir)
```
