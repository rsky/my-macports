# My MacPorts Repository

## SETUP

### 1. Get

```
git clone https://github.com/rsky/my-macports.git
```

### 2. Activate

To activate a local ports repository, insert a following line to */opt/local/etc/macports/sources.conf*.

```
file:///path/to/my-macports/macports [nosync]
```

## INSTALL PORTS

Use `-s` option to force source install.

```
sudo port -s install py27-supervisor
```
