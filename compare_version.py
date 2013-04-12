#!/usr/bin/env python

import re
from glob import glob
from os import path
from distutils.version import LooseVersion

default_ports_dir = '/opt/local/var/macports/sources/rsync.macports.org/release/tarballs/ports'
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

def compare_version(name, default_portfile, private_portfile):
    default_version = read_version(default_portfile)
    private_version = read_version(private_portfile)

    params = {
        'name': name,
        'd_version': default_version,
        'p_version': private_version,
        'sign': '=',
    }

    if default_version > private_version:
        params['sign'] = '>'
    elif default_version < private_version:
        params['sign'] = '<'

    print '%(name)s (%(d_version)s %(sign)s %(p_version)s)' % params

def main():
    portfiles = glob(path.join(private_ports_dir, '*', '*', 'Portfile'))
    ports = []

    for portfile in portfiles:
        components = portfile.split(path.sep)
        default_portfile = path.join(default_ports_dir, *components[-3:])
        if path.exists(default_portfile):
            ports.append((components[-2], default_portfile, portfile))

    ports.sort()

    for name, default_portfile, private_portfile in ports:
        compare_version(name, default_portfile, private_portfile)

if __name__ == '__main__':
    main()
