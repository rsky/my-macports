#!/usr/bin/env python2.7

from __future__ import print_function
import re
from glob import glob
from os import path
from distutils.version import LooseVersion

default_ports_dir = '/opt/local' \
    '/var/macports/sources/rsync.macports.org/release/tarballs/ports'
private_ports_dir = path.join(path.dirname(__file__), 'macports')

version_re = re.compile(r'^version[ \t]+([^ \t\r\n]+)')
revision_re = re.compile(r'^revision[ \t]+([^ \t\r\n]+)')

def read_version(portfile):
    version = None
    revision = None

    for line in open(portfile, 'r'):
        if version is None:
            match = version_re.match(line)
            if match is not None:
                version = match.group(1)
        elif revision is None:
            match = revision_re.match(line)
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
    private_version = read_version(private_portfile)
    default_version = read_version(default_portfile)

    params = {
        'name': name,
        'p_version': private_version,
        'd_version': default_version,
        'sign': '=',
    }

    if private_version > default_version:
        params['sign'] = '>'
    elif private_version < default_version:
        params['sign'] = '<'

    print('{name} ({p_version} {sign} {d_version})'.format(**params))

def main():
    portfiles = glob(path.join(private_ports_dir, '*', '*', 'Portfile'))
    ports = []

    for portfile in portfiles:
        components = portfile.split(path.sep)
        default_portfile = path.join(default_ports_dir, *components[-3:])
        if path.exists(default_portfile):
            ports.append((components[-2], portfile, default_portfile))

    ports.sort()

    for name, private_portfile, default_portfile in ports:
        compare_version(name, private_portfile, default_portfile)

if __name__ == '__main__':
    main()
