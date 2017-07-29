
.. _compile-ossec-mingw: 

OSSEC's Windows agent is compiled using `MinGW <http://www.mingw.org/>`_

.. note::

   This documentation assumes you have MinGW installed, and it is usable. An example of installing MinGW on CentOS is available `here </install-mingw.html>`_

It has always been a pain to generate snapshots for Windows because it required me to open up my Windows VM (slow), push the code there, compile, etc. Well, until this week when I started to play with MinGW cross-compilation feature to completely build an Windows agent from Linux.

How it works? First, you need to install MinGW and `nsis <http://nsis.sourceforge.net/Main_Page>`_ (to build the installer). For OpenSSL support, an OpenSSL MinGW package will also be necessary.

After that, download the source and generate the Windows package directory (replace 2.6 with the latest version or download the latest source from the github `repository <https://github.com/ossec/ossec-hids>`_):

.. include:: getossec.trst

Compiling OSSEC 2.9 with MinGW:
===============================

Change directory to the src directory:

.. code-block:: console

   # cd ossec-hids-2.9.0/src

Now run ``make TARGET=winagent``:

.. code-block:: console

   # make TARGET=winagent

This should produce a good amount of compilation output that ends with:

.. code-block:: console
   
   Output: "ossec-win32-agent.exe"
   Install: 7 pages (448 bytes), 3 sections (3144 bytes), 769 instructions (21532 bytes), 318 strings (32350 bytes), 1 language table (346 bytes).
   Uninstall: 5 pages (320 bytes),
   1 section (1048 bytes), 350 instructions (9800 bytes), 184 strings (3360 bytes), 1 language table (290 bytes).
   Datablock optimizer saved 100205 bytes (~8.1%).

   Using zlib compression.

   EXE header size:               57856 / 56320 bytes
   Install code:                  14832 / 58196 bytes
   Install data:                1045670 / 3116385 bytes
   Uninstall code+data:           21058 / 21474 bytes
   CRC (0x239C5E6F):                  4 / 4 bytes

   Total size:                  1139420 / 3252379 bytes (35.0%)
   make settings
   make[1]: Entering directory `/home/ddp/src/projects/git/github/ddpbsd/ossec-hids/src'

   General settings:
       TARGET:           winagent
       V:
       DEBUG:
       DEBUGAD
       PREFIX:           /var/ossec
       MAXAGENTS:        2048
       DATABASE:
       ONEWAY:           no
       CLEANFULL:        no
   User settings:
       OSSEC_GROUP:      ossec
       OSSEC_USER:       ossec
       OSSEC_USER_MAIL:  ossecm
       OSSEC_USER_REM:   ossecr
   Lua settings:
       LUA_PLAT:         posix
   USE settings:
       USE_ZEROMQ:       no
       USE_GEOIP:        no
       USE_PRELUDE:      no
       USE_OPENSSL:      no
       USE_PICVIZ:       no
       USE_INOTIFY:      no
   Mysql settings:
       includes:
       libs:
   Pgsql settings:
       includes:
       libs:
   Defines:
       -DMAX_AGENTS=2048 -DOSSECHIDS -DDEFAULTDIR="/var/ossec" -DUSER="ossec" -DREMUSER="ossecr" -DGROUPGLOBAL="ossec" -DMAILUSER="ossecm" -DLinux
    Compiler:
       CFLAGS           -O2 -DMAX_AGENTS=2048 -DOSSECHIDS -DDEFAULTDIR="/var/ossec" -DUSER="ossec" -DREMUSER="ossecr" -DGROUPGLOBAL="ossec" -DMAILUSER="ossecm" -DLinux -Wall -Wextra -I./ -I./headers/
       LDFLAGS          -lm
       CC              gcc
       MAKE            make
   make[1]: Leaving directory `/home/ddp/src/projects/git/github/ddpbsd/ossec-hids/src'

   Done building winagent

The final output will be saved to ``./win32/ossec-win32-agent.exe``.



Compiling OSSEC 2.8.x with MinGW:
=================================

Generate the Windows package directory:

.. code-block:: console

    # cd ossec-hids-2.8.3/src/win32
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
