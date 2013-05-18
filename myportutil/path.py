#!python
# -*- coding: utf-8 -*-
"""パス定数を定義する
"""

import os

DEFAULT_PORTS_DIR = '/opt/local' \
    '/var/macports/sources' \
    '/rsync.macports.org/release/tarballs/ports'

PRIVATE_PORTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'ports'))
