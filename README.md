[![Actions Status](https://github.com/dhananjayraut/imdir/workflows/Python%20package/badge.svg)](https://github.com/dhananjayraut/imdir/actions)  
![PyPI page](https://pypi.org/project/imdir/)  

# imdir 

a simple python package to analyse a directory full of images

## Installation

stable version from pypi
```
pip install imdir
```

### or latest from master branch
```bash
pip install git+https://github.com/dhananjayraut/imdir
```
### Dependencies

* matplotlib
* pillow

## Usage
```python
im_dir = image_dir(path="../input/train/") # give path to class

imdir.sc_plot(alpha=0.5) # plot height and width as scatter plot

imdir.width_plot() # plot width as histogram using matplotlib

imdir.height_plot() # plot height as histogram using matplotlib
```

## Documentation
```python
help(imdir.image_dir)
```

### Work In progress