.. _build_makefile:

Makefile
========

Settings
--------

All changes to the makefile that take external input should be reported
via the settings build step. This allows troubleshooting and review of
the evnironment, and the hope is that some new features will become
discovable for other developers.

.. code-block:: console 

    % make DATABASE=mysql TARGET=server USE_ZEROMQ=1 USE_GEOIP=1 settings

    General settings:
        TARGET:          server
        V:
        DEBUG:
        DEBUGAD
        PREFIX:          /var/ossec
        MAXAGENTS:       2048
        DATABASE:        mysql
    User settings:
        OSSEC_GROUP:     ossec
        OSSEC_USER:      ossec
        OSSEC_USER_MAIL: ossecm
        OSSEC_USER_REM:  ossecr
    Lua settings:
        LUA_PLAT:       macosx
    USE settings:
        USE_ZEROMQ:     1
        USE_GEOIP:      1
        USE_PRELUDE:    0
    Mysql settings:
        includes:       -I/usr/include/mysql/
        libs:           -L/usr/lib/mysql -lmysqlclient
    Pgsql settings:
        includes:
        libs:
    Defines:
        -DMAX_AGENTS=2048 -DOSSECHIDS -DDarwin -DHIGHFIRST -DZEROMQ_OUTPUT  -DGEOIP -DUMYSQL
    Compiler:
        CFLAGS          -DMAX_AGENTS=2048 -DOSSECHIDS -DDarwin -DHIGHFIRST -DZEROMQ_OUTPUT  -DGEOIP -DUMYSQL  -Wall -Wextra -O2 -I./ -I./headers/
        LDFLAGS         -lzmq -lczmq -lGeoIP -L/usr/lib/mysql -lmysqlclient
        CC              cc
        MAKE            /Applications/Xcode.app/Contents/Developer/usr/bin/make


