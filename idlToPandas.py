#!/usr/bin/env python

"""
Created on 2014-06-01T20:15:40
"""

from __future__ import division, print_function
import sys


try:
    import argparse
except ImportError:
    print('You need argparse installed')
    sys.exit(1)

try:
    import pandas as pd
except ImportError:
    print('You need pandas installed')
    sys.exit(1)

try:
    from scipy.io.idl import readsav
except ImportError:
    print('You need scipy installed')
    sys.exit(1)


__author__ = "Matt Giguere (github: @mattgiguere)"
__maintainer__ = "Matt Giguere"
__email__ = "matthew.giguere@yale.edu"
__status__ = " Development NOT(Prototype or Production)"
__version__ = '0.0.1'


def idlToPandas(fileName, keyValue):
    """PURPOSE: To restore an IDL strcture contained
    within an IDL save file and add it to a pandas
    data frame."""
    struct = readsav(fileName)

    pdf = pd.DataFrame(struct.keyValue)
    return pdf


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A routine to restore a structure in an IDL save file '
        ' and store the contents in a pandas data frame.')
    parser.add_argument(
        'fileName',
        help='The name of the IDL save structure if there is more than '
        'one.', nargs='?')
    parser.add_argument(
        'keyValue',
        help='The name of the IDL save structure if there is more than '
        'one.', nargs='?')
    if len(sys.argv) > 2:
        print('use the command')
        print('python idlToPandas.py keyValue')
        sys.exit(2)

    args = parser.parse_args()

    idlToPandas(args.fileName, args.keyValue)
