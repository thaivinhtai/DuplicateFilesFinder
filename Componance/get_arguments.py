# -*- coding: utf-8 -*-

"""Get arguments

This module integrates Python-3 argparse lib to collect input data.
"""

from argparse import ArgumentParser


def get_arguments():
    """Collect input data.

    This function get one argument after specified -p/--path flag.

    Returns
    -------
    string
        list of all data.
    """
    parser = ArgumentParser(description="find duplicate file.")
    parser.add_argument("-p", "--path", type=str, required=True,
                        help=("accepts one mandatory argument" +
                              "that identifies the root directory" +
                              "to start scanning for duplicate files"))
    return parser.parse_args().path
