# -*- coding: utf-8 -*-

"""This module marks the folder as a python package and do some import."""

from .get_arguments import get_arguments
from .scan_files import scan_files
from .group_files_by_size import group_files_by_size
from .generate_hash import generate_hash
from .group_files_by_checksum import group_files_by_checksum
from .find_duplicate_files import find_duplicate_files
from .optimize_performance import group_same_files
