--- setup.py.orig	2012-11-01 17:09:06.000000000 +0900
+++ setup.py	2012-11-10 14:07:41.000000000 +0900
@@ -72,12 +72,12 @@
 NAME = 'Pillow'
 VERSION = '1.7.8'
 PIL_VERSION = '1.1.7'
-TCL_ROOT = None
-JPEG_ROOT = None
-ZLIB_ROOT = None
-TIFF_ROOT = None
-FREETYPE_ROOT = None
-LCMS_ROOT = None
+TCL_ROOT = '__PREFIX__/lib', '__PREFIX__/include'
+JPEG_ROOT = '__PREFIX__/lib', '__PREFIX__/include'
+ZLIB_ROOT = '__PREFIX__/lib', '__PREFIX__/include'
+TIFF_ROOT = '__PREFIX__/lib', '__PREFIX__/include'
+FREETYPE_ROOT = '__PREFIX__/lib', '__PREFIX__/include/freetype2'
+LCMS_ROOT = '__PREFIX__/lib', '__PREFIX__/include'
 
 
 class pil_build_ext(build_ext):
