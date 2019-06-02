# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('clearmkvcnames/clearmkvcnames.py').read(),
    re.M
    ).group(1)


# with open("README.rst", "rb") as f:
#     long_descr = f.read().decode("utf-8")


setup(
    name = "clear-mkvcnames",
    packages = ["clearmkvcnames"],
    entry_points = {
        "console_scripts": ['clear-mkvcnames = clearmkvcnames.clearmkvcnames:main']
        },
    version = version,
    description = "This command-line tool clears the chapter names defined in an MKV file.",
    long_description = "This command-line tool clears the chapter names defined in an MKV file.",
    author = "Joe Arauzo",
    author_email = "joe@arauzo.net",
    url = "https://github.com/JoeArauzo/clear-mkvcnames",
    )
