.. _compile-ossec-mingw: 

OSSEC's Windows agent is compiled using `MinGW <http://www.mingw.org/>`_

.. note::

   This documentation assumes you have MinGW installed, and it is usable. An example of installing MinGW on CentOS is available `here <install-mingw.html>`_.

Requirements
^^^^^^^^^^^^

* `MinGW <http://www.mingw.org/>`_

* `nsis <http://nsis.sourceforge.net/Main_Page>`_

* `OpenSSL <https://www.openssl.org/>`_/`LibreSSL <https://www.libressl.org/>`_ (optional)

.. versionadded:: 3.3

* PCRE2 source tree in `src/external`


Compilation
^^^^^^^^^^^

Change directory to the src directory:

.. code-block:: console

   # cd ossec-hids-XXX/src

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



.. This document is a copy of Daniel Cid's blogpost `Compiling the Windows Agent from a Linux system <http://dcid.me/2009/06/compiling-the-windows-agent-from-a-linux-system/>`_
