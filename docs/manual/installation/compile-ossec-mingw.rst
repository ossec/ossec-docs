
.. _compile-ossec-mingw: 

Compiling OSSEC with ming:
==========================


OSSEC's Windows agent is compiled using `MinGW <http://www.mingw.org/>`_


It has always been a pain to generate snapshots for Windows because it required me to open up my Windows VM (slow), push the code there, compile, etc. Well, until this week when I started to play with MinGW cross-compilation feature to completely build an Windows agent from Linux.

How it works? First, you need to install MinGW and `nsis <http://nsis.sourceforge.net/Main_Page>`_ (to build the installer). For OpenSSL support, an OpenSSL MinGW package will also be necessary.


After that, download the source and generate the Windows package directory (replace 2.6 with the latest version or download the latest source `here <https://bitbucket.org/dcid/ossec-hids/get/tip.tar.gz>`_):

.. include:: getossec.trst


And generate the Windows package directory:

.. code-block:: console

    # cd ossec-hids-2.8/src/win32
    # ./gen-win.sh

Now, you will have the win-pkg directory under src. Just go there and run make.sh. Your Windows agent package should be created in a few minutes:

.. note:: The ``make.sh`` script may require modification depending on the Linux distribution used.

.. code-block:: console

    # cd ../win-pkg
    # sh ./make.sh

You will see the following in the screen:


.. code-block:: console

    Making windows agent
    rootcheck/win-common.c: In function "__os_winreg_querykey":
    rootcheck/win-common.c:279: warning: pointer targets in passing argument 7 of "RegEnumValueA" differ in signedness
    win-registry.c: In function "os_winreg_querykey":
    ...

    Output: "ossec-win32-agent.exe"
    Install: 7 pages (448 bytes), 3 sections (3144 bytes), 379 instructions (10612 bytes), 247 strings (42580 bytes), 1 language table (346 bytes).
    Uninstall: 5 pages (320 bytes),
    1 section (1048 bytes), 301 instructions (8428 bytes), 166 strings (2646 bytes), 1 language table (290 bytes).
    Datablock optimizer saved 8371 bytes (~0.7%).

Which means that your agent executable ossec-win32-agent.exe has been created properly.




.. This document is a copy of Daniel Cid's blogpost `Compiling the Windows Agent from a Linux system <http://dcid.me/2009/06/compiling-the-windows-agent-from-a-linux-system/>`_
