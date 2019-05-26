#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script accepts one mandatory argument -p or --path that identifies the
root directory to start scanning for duplicate files.
"""

from json import dumps
from Componance import get_arguments, scan_files, find_duplicate_files


def main():
    """main flow"""
    result = find_duplicate_files(scan_files(get_arguments()))
    return print(dumps(result) if result else "", end="")


if __name__ == "__main__":
    main()
