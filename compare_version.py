#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""独自のportと標準のportのバージョンを比較する
"""

from __future__ import print_function
import re
from distutils.version import LooseVersion
from myportutil.util import find_common_ports

VERSION_PATTERN = re.compile(r'version[ \t]+([^ \t\r\n]+)')
REVISION_PATTERN = re.compile(r'revision[ \t]+([^ \t\r\n]+)')


def read_version(portfile):
    """Portfileからバージョンを取得する
    """
    version = None
    revision = None

    for line in open(portfile, 'r'):
        if version is None:
            match = VERSION_PATTERN.match(line)
            if match is not None:
                version = match.group(1)
        elif revision is None:
            match = REVISION_PATTERN.match(line)
            if match is not None:
                revision = match.group(1)
        else:
            break

    if version is None:
        version = '0'
    if revision is None:
        revision = '0'

    return LooseVersion(version + '_' + revision)


def compare_version(name, private_portfile, default_portfile):
    """portのバージョンを比較・表示する
    """
    private_version = read_version(private_portfile)
    default_version = read_version(default_portfile)
    sign = '='

    if private_version > default_version:
        sign = '>'
    elif private_version < default_version:
        sign = '<'

    print('{name} ({pv} {sign} {dv})'.format(
          name=name, sign=sign,
          pv=private_version, dv=default_version))


def main():
    """main
    """
    for name, private_portfile, default_portfile in find_common_ports():
        compare_version(name, private_portfile, default_portfile)

if __name__ == '__main__':
    main()
