#!python
# -*- coding: utf-8 -*-
"""ユーティリティ関数を定義する"""

from __future__ import absolute_import
import os, re, subprocess
from glob import glob
from .path import DEFAULT_PORTS_DIR, PRIVATE_PORTS_DIR


CATEGORY_PATTERN = re.compile(r'\((\w+)')

def get_category(port):
    """port info を叩いてカテゴリを判定する"""
    try:
        info = subprocess.check_output(['port', 'info', port])
    except subprocess.CalledProcessError:
        return None

    match = CATEGORY_PATTERN.search(info)
    if not match:
        return None

    return match.group(1)

def find_common_ports():
    """独自のportと標準のport両方が存在するもののリストを返す"""
    portfiles = glob(os.path.join(PRIVATE_PORTS_DIR, '*', '*', 'Portfile'))
    ports = []

    for portfile in portfiles:
        components = portfile.split(os.path.sep)
        default_portfile = os.path.join(DEFAULT_PORTS_DIR, *components[-3:])
        if os.path.exists(default_portfile):
            ports.append((components[-2], portfile, default_portfile))

    ports.sort()
    return ports
