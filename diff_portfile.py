#!/usr/bin/env python

from __future__ import print_function
import re, sys, subprocess
from os import path

default_ports_dir = '/opt/local/var/macports/sources/rsync.macports.org/release/tarballs/ports'
private_ports_dir = path.join(path.dirname(__file__), 'macports')
category_pattern = re.compile(r'\((\w+)')

def get_category(port):
    try:
        info = subprocess.check_output(['port', 'info', port])
    except subprocess.CalledProcessError:
        return None

    match = category_pattern.search(info)
    if not match:
        return None

    return match.group(1)

def diff(port, diff_cmd='diff'):
    category = get_category(port)
    if not category:
        return

    default_port = path.join(default_ports_dir, category, port, 'Portfile')
    private_port = path.join(private_ports_dir, category, port, 'Portfile')
    for port in (default_port, private_port):
        if not path.exists(port):
            print(port, 'does not exist.', file=sys.stderr)
            return

    subprocess.call([diff_cmd, '-u', default_port, private_port])

def main():
    diff_cmd = 'diff'
    if sys.stdout.isatty():
        diff_cmd = 'colordiff'
    for port in sys.argv[1:]:
        diff(port, diff_cmd=diff_cmd)

if __name__ == '__main__':
    main()
