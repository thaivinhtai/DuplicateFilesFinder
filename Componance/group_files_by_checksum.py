# -*- coding: utf-8 -*-

"""Group Files by their Checksum.

This module contains a function group_files_by_checksum that takes one argument
file_path_names, corresponding to a flat list of the absolute path and
name of files, and that returns a list of groups of duplicate files.
"""

from .generate_hash import generate_hash


def group_files_by_checksum(file_path_names):
    """Group Files by their Checksum.

    This function takes one argument file_path_names, corresponding to a flat
    list of the absolute path and name of files and returns a list of groups of
    duplicate files.

    Parameters
    ----------
    file_path_names : list
        list of files.

    returns
    -------
    list
        a nested list of groups of duplicate files.
    """
    identify_group = {}
    for filename in file_path_names:
        checksum = generate_hash(filename)
        if checksum is None:
            continue
        if checksum in identify_group.keys():
            identify_group[checksum].append(filename)
        else:
            identify_group[checksum] = [filename]
    return [group for group in identify_group.values() if len(group) > 1]
