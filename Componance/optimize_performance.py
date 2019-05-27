# -*- coding: utf-8 -*-

"""Performance Optimization.

This module uses another method to find duplicate files that would be much
faster than using a hash algorithm.
"""

import os
import stat


def _compare_two_files(filename1, filename2):
    """Compare two files.

    This function check if the two file have exactly the same content.

    Parameters
    ----------
    filename1 : string
        full path of filename 1.
    filename2 : string
        full path of filename 2.

    Returns
    -------
    bool
        True - if they have same content.
        False - if not.
    """
    file1_info = (stat.S_IFMT(os.stat(filename1).st_mode),
                  os.stat(filename1).st_size, os.stat(filename1).st_mtime)
    file2_info = (stat.S_IFMT(os.stat(filename2).st_mode),
                  os.stat(filename2).st_size, os.stat(filename2).st_mtime)
    if file1_info[0] != stat.S_IFREG or file2_info[0] != stat.S_IFREG:
        return False
    if file1_info == file2_info:
        return True
    if file1_info[1] != file2_info[1]:
        return False

    cache = {}
    outcome = cache.get((filename1, filename2, file1_info, file2_info))
    if outcome is None:
        bufsize = 8 * 1024
        with open(filename1, 'rb') as fp1, open(filename2, 'rb') as fp2:
            while True:
                buf1 = fp1.read(bufsize)
                buf2 = fp2.read(bufsize)
                if buf1 != buf2:
                    outcome = False
                    break
                if not buf1:
                    outcome = True
                    break
        if len(cache) > 100:
            cache.clear()
        cache[filename1, filename2, file1_info, file2_info] = outcome
    return outcome


def group_same_files(file_path_names):
    """Group same content files.

    This function takes one mandatory argument file_path_names corresponding
    to a flat list of absolute file path names, and that returns a list of
    groups of at least two files that have the same content.

    Parameters
    ----------
    file_path_names : list
        list path name of files.

    returns
    -------
    list
        a nested list of groups of at least two files
        that have the same content.
    """
    group_files = []
    filenames = list(file_path_names)
    while filenames:
        current_file = filenames[0]
        group_by_comparing = [current_file]
        for file in filenames[1:]:
            if _compare_two_files(current_file, file):
                group_by_comparing.append(file)
        filenames = list(set(filenames) - set(group_by_comparing))
        if len(group_by_comparing) > 1:
            group_files.append(group_by_comparing)
    return group_files
