# My MacPorts Repository

## SETUP

### 1. Get

```
git clone https://github.com/rsky/my-macports.git
```

### 2. Make Index

```
cd my-macports/ports && portindex
```

### 3. Activate

To activate this ports repository, insert a following line to */opt/local/etc/macports/sources.conf*.

```
file:///path/to/my-macports/ports
```

The git repository will be synchronized by `port sync` or `port selfupdate` from next time. And the PortIndex also will be updated same time.

## INSTALL PORTS

Use `-s` option to force source install.

```
sudo port -s install peg
```
