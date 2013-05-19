#!/bin/bash
cd "$(dirname "$0")"
find ports -mindepth 2 -maxdepth 2 -type d -print0 | xargs -0 port livecheck
