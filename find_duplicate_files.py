#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script accepts one mandatory argument -p or --path that identifies the
root directory to start scanning for duplicate files.
"""

from json import dumps
from Componance import (get_arguments, scan_files,
                        find_duplicate_files, group_same_files)


def _print_result(result):
    """Print result.

    This function print a non empty list in Json format.

    Parameters
    ----------
    result : list
        a nested list of group of duplicate files.

    Returns
    -------
    object
        print object with attribute 'end=""'.
    """
    return print(dumps(result, indent=4) + "\n" if result else "", end="")


def main():
    """main flow"""
    file_path_names, performance = get_arguments()
    if performance:
        return _print_result(group_same_files(scan_files(file_path_names)))
    return _print_result(find_duplicate_files(scan_files(file_path_names)))


if __name__ == "__main__":
    main()
