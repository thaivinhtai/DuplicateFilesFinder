# -*- coding: utf-8 -*-

"""Group files by thier size.

This module groups files that has same size.
"""

from os.path import getsize


def group_files_by_size(file_path_names):
    """Group files by thier size.

    This function takes one mandatory argument file_path_names corresponding
    to a flat list of absolute file path names, and that returns a list of
    groups of at least two files that have the same size.

    Parameters
    ----------
    file_path_names : list
        list path name of files.

    returns
    -------
    list
        a nested list of groups of at least two files that have the same size.
    """
    groups = {}
    for filename in file_path_names:
        size = getsize(filename)
        if size == 0:
            continue
        if size in groups.keys():
            groups[size].append(filename)
        else:
            groups[size] = [filename]
    return [group for group in groups.values() if len(group) > 1]
