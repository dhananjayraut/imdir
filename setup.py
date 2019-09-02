import setuptools

with open("./README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='imdir',

     version='0.1.dev1',

     author="Dhananjay Raut",

     author_email="rautdhananjay33@gmail.com",

     description="A package to analyse a directory full of images",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/",

     packages=setuptools.find_packages(),

     classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
     py_modules=["imdir"],
     install_requires=['pillow', 'matplotlib'],
 )
