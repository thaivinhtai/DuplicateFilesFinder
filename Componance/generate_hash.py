# -*- coding: utf-8 -*-

"""Generate a Hash Value for a File

The content of a file can be reduced to a checksum.

The actual procedure which yields the checksum from the file's content is
called a checksum function or checksum algorithm.

There are many cryptographic hash algorithms. The MD5 message-digest algorithm
is a widely used hash function producing a 128-bit hash value. The MD5
algorithm can be used to generate a compact digital fingerprint of a file.

Files that have the same content are identified with the same hash value.

Notes
-----
    It is very unlikely that any two non-identical files in the real world will
    have the same MD5 hash.
"""

from hashlib import md5


def generate_hash(filename):
    """Generate a hash value for a file.

    This function uses MD5 algorithm to generate a hash value for a file.

    Parameters
    ----------
    filename : string
        name of a file, full path is included.

    Returns
    -------
    string
        Hash value of file.
    """
    try:
        with open(filename, "rb") as f:
            hash_md5 = md5(f.read())
        return hash_md5.hexdigest()
    except PermissionError:
        return None
