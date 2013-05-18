#!/usr/bin/env python2.7

from __future__ import print_function
import os, re, sys, subprocess
from myportutil.path import default_ports_dir, private_ports_dir

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

    default_port = os.path.join(default_ports_dir, category, port, 'Portfile')
    private_port = os.path.join(private_ports_dir, category, port, 'Portfile')
    for port in (default_port, private_port):
        if not os.path.exists(port):
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
