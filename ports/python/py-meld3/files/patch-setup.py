--- setup.py.orig	2012-09-13 01:08:18.000000000 +0900
+++ setup.py	2012-09-26 12:15:07.000000000 +0900
@@ -1,3 +1,5 @@
+from ez_setup import use_setuptools
+use_setuptools()
 from distutils.core import setup, Extension
 import os
 import sys
