# -*- coding: utf-8 -*-

"""Scan files

This module integrates Python3 os.walk function to retrieve the list of files
in every directory in the tree rooted at directory path.
"""

from os.path import expanduser, realpath, islink, join
from os import walk


def get_full_path(file):
    """Get full path of file.

    This function retrieves full path of the given file.

    Parameters
    ----------
    file : str
        file name.

    Returns
    -------
    string
        Full path of file.
    """
    if file[0] == '~':
        file = expanduser(file)
    else:
        file = realpath(file)
    return file


def scan_files(path):
    """Scan recursively from this specified path.

    This function takes one argument path corresponding to an absolute path,
    and that returns a flat list of files scanned recursively from this
    specified path.

    Parameters
    ----------
    path : str
        path of a folder.

    Returns
    -------
    list
        a flat list of files' absolute path name scanned recursively from
        specified path.
    """
    path = get_full_path(path)
    files_list = []
    for direc, subdir, files in walk(path):
        del subdir
        files_list.extend([join(direc, file) for file in files])
    files_list = [file for file in files_list if not islink(file)]
    return files_list
