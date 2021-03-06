# -*- coding: utf-8 -*-


"""clearmkvcnames.myutils: myutils module within the clearmkvcnames package."""


import logging
from pathlib import Path

def initclogger(name):
    """This function sets up console logging and returns a logger object."""

    # Create a customer logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    c_formatter = logging.Formatter('%(levelname)s: %(message)s')
    c_handler.setFormatter(c_formatter)

    # # Add handlers to the logger
    logger.addHandler(c_handler)

    return logger


def pathwoconflict(filepath):
    """
    This function inspects the filepath and returns a filepath with a filename
    that will not conflict with any preexisting file.
    """

    filepath = str(filepath)
    filepath = Path(filepath)
    basename = filepath.stem
    c = 1
    while filepath.exists():
        filename = basename + f" {c}" + filepath.suffix
        filepath = filepath.parent / filename
        c += 1
    
    return filepath