--- setup.py.orig	2012-02-16 20:10:20.000000000 +0900
+++ setup.py	2012-09-30 19:41:17.000000000 +0900
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
@@ -98,7 +98,7 @@
         if sys.platform == "cygwin":
             # pythonX.Y.dll.a is in the /usr/lib/pythonX.Y/config directory
             _add_directory(library_dirs, os.path.join(
-                "/usr/lib", "python%s" % sys.version[:3], "config"))
+                "/usr/lib", "python" + sys.version[:3], "config"))
 
         elif sys.platform == "darwin":
             # attempt to make sure we pick freetype2 over other versions
@@ -159,8 +159,8 @@
                 TCL_ROOT = os.path.abspath(TCL_ROOT)
                 if os.path.isfile(os.path.join(TCL_ROOT, "include", "tk.h")):
                     # FIXME: use distutils logging (?)
-                    print "--- using Tcl/Tk libraries at", TCL_ROOT
-                    print "--- using Tcl/Tk version", TCL_VERSION
+                    print("--- using Tcl/Tk libraries at", TCL_ROOT)
+                    print("--- using Tcl/Tk version", TCL_VERSION)
                     TCL_ROOT = _lib_include(TCL_ROOT)
                     break
             else:
@@ -280,7 +280,7 @@
             defs.append(("HAVE_LIBZ", None))
         if sys.platform == "win32":
             libs.extend(["kernel32", "user32", "gdi32"])
-        if struct.unpack("h", "\0\1")[0] == 1:
+        if struct.unpack(r"h", struct.pack(r"bb", 0, 1))[0] == 1:
             defs.append(("WORDS_BIGENDIAN", None))
 
         exts = [(Extension(
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
@@ -353,15 +332,15 @@
 
     def summary_report(self, feature, unsafe_zlib):
 
-        print "-" * 68
-        print "SETUP SUMMARY (Pillow", VERSION, "/ PIL %s)" % PIL_VERSION
-        print "-" * 68
-        print "version      ", VERSION
+        print("-" * 68)
+        print("SETUP SUMMARY (Pillow {0}/ PIL {1})".format(VERSION, PIL_VERSION))
+        print("-" * 68)
+        print("version      ", VERSION)
         v = string.split(sys.version, "[")
-        print "platform     ", sys.platform, string.strip(v[0])
+        print("platform     ", sys.platform, string.strip(v[0]))
         for v in v[1:]:
-            print "             ", string.strip("[" + v)
-        print "-" * 68
+            print("             ", string.strip("[" + v))
+        print("-" * 68)
 
         options = [
             (feature.tcl and feature.tk, "TKINTER"),
@@ -375,34 +354,34 @@
         all = 1
         for option in options:
             if option[0]:
-                print "---", option[1], "support available"
+                print("---", option[1], "support available")
             else:
-                print "***", option[1], "support not available",
+                print("***", option[1], "support not available", end=' ')
                 if option[1] == "TKINTER" and _tkinter:
                     version = _tkinter.TCL_VERSION
-                    print "(Tcl/Tk %s libraries needed)" % version,
-                print
+                    print("(Tcl/Tk {0} libraries needed)".format(version), end=' ')
+                print()
                 all = 0
 
         if feature.zlib and unsafe_zlib:
-            print
-            print "*** Warning: zlib", unsafe_zlib,
-            print "may contain a security vulnerability."
-            print "*** Consider upgrading to zlib 1.2.3 or newer."
-            print "*** See: http://www.kb.cert.org/vuls/id/238678"
-            print " http://www.kb.cert.org/vuls/id/680620"
-            print " http://www.gzip.org/zlib/advisory-2002-03-11.txt"
-            print
+            print()
+            print("*** Warning: zlib", unsafe_zlib, end=' ')
+            print("may contain a security vulnerability.")
+            print("*** Consider upgrading to zlib 1.2.3 or newer.")
+            print("*** See: http://www.kb.cert.org/vuls/id/238678")
+            print(" http://www.kb.cert.org/vuls/id/680620")
+            print(" http://www.gzip.org/zlib/advisory-2002-03-11.txt")
+            print()
 
-        print "-" * 68
+        print("-" * 68)
 
         if not all:
-            print "To add a missing option, make sure you have the required"
-            print "library, and set the corresponding ROOT variable in the"
-            print "setup.py script."
-            print
+            print("To add a missing option, make sure you have the required")
+            print("library, and set the corresponding ROOT variable in the")
+            print("setup.py script.")
+            print()
 
-        print "To check the build, run the selftest.py script."
+        print("To check the build, run the selftest.py script.")
 
     def check_zlib_version(self, include_dirs):
         # look for unsafe versions of zlib
