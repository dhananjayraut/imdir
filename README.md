# imdir
a simple python package to analyse a directory full of images  
How many times you want to see what all types of images have in a directory
this simple package just helps with that

### WIP

## Installation
```bash
pip install git+https://github.com/dhananjayraut/imdir
```
### dependencies

* matplotlib
* pillow

## Usage
```python
im_dir = image_dir(path="../input/train/") # give path to class

imdir.sc_plot() # plot height and width as scatter plot

imdir.width_plot() # plot width as histogram using matplotlib

imdir.height_plot() # plot height as histogram using matplotlib
```

## Documentation

___
