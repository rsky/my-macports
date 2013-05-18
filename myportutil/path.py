#!python
import os
default_ports_dir = '/opt/local' \
    '/var/macports/sources' \
    '/rsync.macports.org/release/tarballs/ports'
private_ports_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'ports'))
