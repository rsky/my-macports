--- setup.py.orig	2012-02-16 20:10:20.000000000 +0900
+++ setup.py	2012-09-30 19:06:34.000000000 +0900
@@ -73,12 +73,12 @@
 NAME = 'Pillow'
 VERSION = '1.7.7'
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
@@ -159,8 +159,8 @@
                 TCL_ROOT = os.path.abspath(TCL_ROOT)
                 if os.path.isfile(os.path.join(TCL_ROOT, "include", "tk.h")):
                     # FIXME: use distutils logging (?)
-                    print "--- using Tcl/Tk libraries at", TCL_ROOT
-                    print "--- using Tcl/Tk version", TCL_VERSION
+                    print "--- using Tcl/Tk libraries at %s" % TCL_ROOT
+                    print "--- using Tcl/Tk version %" % TCL_VERSION
                     TCL_ROOT = _lib_include(TCL_ROOT)
                     break
             else:
@@ -308,28 +308,7 @@
             exts.append(Extension(
                 "_imagingcms", ["_imagingcms.c"], libraries=["lcms"] + extra))
 
-        if sys.platform == "darwin":
-            # locate Tcl/Tk frameworks
-            frameworks = []
-            framework_roots = [
-                "/Library/Frameworks",
-                "/System/Library/Frameworks"]
-            for root in framework_roots:
-                if (os.path.exists(os.path.join(root, "Tcl.framework")) and
-                    os.path.exists(os.path.join(root, "Tk.framework"))):
-                    print "--- using frameworks at", root
-                    frameworks = ["-framework", "Tcl", "-framework", "Tk"]
-                    dir = os.path.join(root, "Tcl.framework", "Headers")
-                    _add_directory(self.compiler.include_dirs, dir, 0)
-                    dir = os.path.join(root, "Tk.framework", "Headers")
-                    _add_directory(self.compiler.include_dirs, dir, 1)
-                    break
-            if frameworks:
-                exts.append(Extension(
-                    "_imagingtk", ["_imagingtk.c", "Tk/tkImaging.c"],
-                    extra_compile_args=frameworks, extra_link_args=frameworks))
-                feature.tcl = feature.tk = 1  # mark as present
-        elif feature.tcl and feature.tk:
+        if feature.tcl and feature.tk:
             exts.append(Extension(
                 "_imagingtk", ["_imagingtk.c", "Tk/tkImaging.c"],
                 libraries=[feature.tcl, feature.tk]))
@@ -354,13 +333,13 @@
     def summary_report(self, feature, unsafe_zlib):
 
         print "-" * 68
-        print "SETUP SUMMARY (Pillow", VERSION, "/ PIL %s)" % PIL_VERSION
+        print "SETUP SUMMARY (Pillow %s/ PIL %s)" % (VERSION, PIL_VERSION)
         print "-" * 68
-        print "version      ", VERSION
+        print "version       %s" % VERSION
         v = string.split(sys.version, "[")
-        print "platform     ", sys.platform, string.strip(v[0])
+        print "platform      %s" % sys.platform, string.strip(v[0])
         for v in v[1:]:
-            print "             ", string.strip("[" + v)
+            print "              %s" % string.strip("[" + v)
         print "-" * 68
 
         options = [
@@ -375,9 +354,9 @@
         all = 1
         for option in options:
             if option[0]:
-                print "---", option[1], "support available"
+                print "--- % support available" %  option[1]
             else:
-                print "***", option[1], "support not available",
+                print "*** %s support not available" % option[1]
                 if option[1] == "TKINTER" and _tkinter:
                     version = _tkinter.TCL_VERSION
                     print "(Tcl/Tk %s libraries needed)" % version,
@@ -386,7 +365,7 @@
 
         if feature.zlib and unsafe_zlib:
             print
-            print "*** Warning: zlib", unsafe_zlib,
+            print "*** Warning: zlib %s" % unsafe_zlib,
             print "may contain a security vulnerability."
             print "*** Consider upgrading to zlib 1.2.3 or newer."
             print "*** See: http://www.kb.cert.org/vuls/id/238678"
