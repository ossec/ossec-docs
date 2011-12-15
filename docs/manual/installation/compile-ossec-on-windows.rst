
.. _compile-ossec-on-windows: 

Compiling OSSEC on Windows:
===========================

Originally posted `Compiling the OSSEC Windows Agent on Windows <http://www.immutablesecurity.com/index.php/2010/07/06/compiling-the-ossec-agent-on-windows/>`_ by `mstarks <http://www.immutablesecurity.com/index.php/author/mstarks/>`_, duplicated here with permission. 

Compiling the OSSEC Windows Agent on Windows
============================================

Most people that use the OSSEC Windows agent `download a pre-compiled <http://www.ossec.net/main/downloads/>`_ copy from the OSSEC site. While that is a good option for many individual users, it may not suit those with more specific needs and/or those in enterprise environments. Users who fall into those categories could benefit from customizing the agent and maintaining internal builds in order to suit their individual needs.

There are already instructions on `how to compile the Windows agent on Linux <http://dcid.me/2009/06/compiling-the-windows-agent-from-a-linux-system/>`_, but ironically the process doesn't work so well on Windows. I had a need to make this work on Windows, so I thought I would share the process with you.

First, there are some prerequisites.  You.ll need:

* The `Nullsoft Scriptable Install System <http://nsis.sourceforge.net/Download>`_ (NSIS)
* The `Minimalist GNU for Windows (MinGW) compiler http://sourceforge.net/downloads/mingw/>`_
* My `batch file. <http://www.immutablesecurity.com/wp-content/wp_uploads/gen_win.txt>`_  Simply rename from gen_win.txt to gen_win.cmd.
* `7-Zip for Windows <http://www.7-zip.org/download.html>`_
* The public domain `Unix2DOS utility <http://www.efgh.com/software/unix2dos.htm>`_
* The latest OSSEC for Unix/Linux <http://www.ossec.net/main/downloads/>`_ (this contains the Windows source code)

Here are the steps:
===================

#. Download and install the required programs. Be sure to pay special attention to the `steps for properly installing and configuring MinGW <http://www.mingw.org/wiki/Getting_Started>`_, particularly the part about modifying the PATH environment variable.
#. Next, we.re going to extract OSSEC using 7-Zip. To do so, simply right-click on the file and select 7-Zip, extract to "folder name.tar," where folder name is the name of the package. This decompresses the archive. Navigate within that folder and repeat this step to untar the archive. At this point, you should see all of the files in the package.
#. Place gen_win.txt in the src\win32 folder and rename the extension to .cmd.
#. Download Unix2DOS and place it in the src\win32 folder
#. Open a command prompt. Navigate to src\win32, make any desired customizations, and execute gen_win.cmd. This should gather all of the required files and place them in src\win-pkg.
#. Next, we compile the Windows agent by navigating to src\win-pkg and executing make.bat (I assume you have the chops to know how to change directories :) ).
#. Now we have all of the files we need but no way to effectively install it. To generate the installer, simply execute the NSIS compiler like so: ``"c:\Program Files\NSIS\makensis.exe" ossec-installer.nsi``

If you see no errors and a binary named ossec-win32-agent.exe, everything was successful. Congratulations, you now have a custom-made version of OSSEC!





