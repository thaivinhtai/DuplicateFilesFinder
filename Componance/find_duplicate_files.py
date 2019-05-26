# -*- coding: utf-8 -*-

"""Find all Duplicate Files.

This module contains function find_duplicate_files that takes one mandatory
argument file_path_names, corresponding to a list of absolute path and name of
files, and that returns a list of groups of duplicate files.
"""

from .group_files_by_size import group_files_by_size
from .group_files_by_checksum import group_files_by_checksum


def find_duplicate_files(file_path_names):
    """Find all Duplicate Files.

    This function groups all duplicate files.

    Parameters
    ----------
    file_path_names : list
        list of files.

    returns
    -------
    list
        a nested list of groups of duplicate files.
    """
    groups_duplicate_file = []
    for groups_by_size in group_files_by_size(file_path_names):
        groups_duplicate_file += group_files_by_checksum(groups_by_size)
    return [group for group in groups_duplicate_file if len(group) > 1]
