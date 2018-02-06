#!python
# -*- coding: utf-8 -*-
"""パス定数を定義する
"""

import os

SOURCES_DIR = '/opt/local/var/macports/sources/rsync.macports.org'

for subdir in ('macports/release/tarballs/ports', 'release/tarballs/ports'):
    path = os.path.join(SOURCES_DIR, subdir)
    print(path)
    if os.path.exists(path):
        DEFAULT_PORTS_DIR = path
        break
else:
    DEFAULT_PORTS_DIR = None

PRIVATE_PORTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'ports'))
