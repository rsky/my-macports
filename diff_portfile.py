#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""独自のPortfileと標準のPortfileの差分を取る
"""

from __future__ import print_function
import os, sys, subprocess
from myportutil import util
from myportutil.path import DEFAULT_PORTS_DIR, PRIVATE_PORTS_DIR

def diff(port, category=None, diff_cmd='diff'):
    """指定したportのPortfileの差分を取る
    """
    if category is None:
        category = util.get_category(port)
        if category is None:
            print('Cannot determine category for port {0}.'.format(port),
                  file=sys.stderr)
            return

    default_portfile = os.path.join(DEFAULT_PORTS_DIR,
                                    category, port, 'Portfile')
    private_portfile = os.path.join(PRIVATE_PORTS_DIR,
                                    category, port, 'Portfile')
    for portfile in (default_portfile, private_portfile):
        if not os.path.exists(portfile):
            print('{0}: {1} does not exist.'.format(port, portfile),
                  file=sys.stderr)
            return

    subprocess.call([diff_cmd, '-u', default_portfile, private_portfile])

def main():
    """main
    """
    diff_cmd = 'diff'
    if sys.stdout.isatty():
        diff_cmd = 'colordiff'

    if len(sys.argv) < 2:
        for port in util.find_common_ports():
            category = port[1].split(os.path.sep)[-3]
            diff(port[0], category=category, diff_cmd=diff_cmd)
    else:
        for port in sys.argv[1:]:
            diff(port, diff_cmd=diff_cmd)

if __name__ == '__main__':
    main()
