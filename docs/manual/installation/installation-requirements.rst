.. _install_req:

Installations requirements
==========================

For UNIX systems, OSSEC only requires gnu make, gcc, and libc.
OpenSSL is a suggested, but optional, prerequisite. 
However, you always have the option to pre-compile
it on one system and move the binaries to the final box.

PCRE2
-----

.. versionadded:: 3.3

PCRE2 has been added to version 3.3. The build system can either use the system's PCRE2 libraries,
or the necessary bits can be built as part of the installation process.

The default build process expects the `pcre2-10.32` source to be installed in `src/external`:

.. code-block:: console

   $ cd ossec-hids-*/src
   $ wget https://ftp.pcre.org/pub/pcre/pcre2-10.32.tar.gz
   $ tar xzf pcre2-10.32.tar.gz -C src/external

To use the system's PCRE2, set the `PCRE2_SYSTEM` variable to yes:

.. code-block:: console

   # cd ossec-hids-*
   # PCRE2_SYSTEM=yes ./install.sh

zlib
----

`zlib <https://www.zlib.net/>`_ is included with OSSEC in `src/external/zlib-1.2.11`. In previous
versions this included version was used by default during the build process, but this changed to 
using the system zlib. Ensure the correct zlib development packages are installed.

To use the included version of zlib, simply set `ZLIB_SYSTEM` to `no`:

.. code-block:: console

   # cd ossec-hids-*
   # ZLIB_SYSTEM=no ./install.sh

Ubuntu
------

On Ubuntu you will need the *build-essential* package in order to
compile and install OSSEC.

To install the package run the following command.

.. code-block:: console

    # apt-get install build-essential zlib1g-dev

To use the system's pcre2 libraries, install the libpcre2 development package:

.. code-block:: console

   # apt-get install libpcre2-dev

If database support is needed *mysql-dev* or *postgresql-dev* should be
installed. Run the following command to install these packages.

.. code-block:: console 

    # apt-get install mysql-dev postgresql-dev

To use the SQLite features, the `libsqlite3-dev` package is necessary.

.. versionadded:: 3.0

.. code-block:: console

   # apt-get install libsqlite3-dev


RedHat
------

RedHat should have most of the packages needed by default. The zlib development package
should be installed:

.. code-block:: console

   # yum install zlib-devel

To use the system's pcre2 libraries, add the pcre2 development package:

.. code-block:: console

   # yum install pcre2-devel

If database support is needed the package mysql-devel and/or postgresql-devel will
need to be installed.

.. code-block:: console

    # yum install mysql-devel postgresql-devel

To use the SQLite features, the `sqlite-devel` package is necessary.

.. versionadded:: 3.0

.. code-block:: console

   # yum install sqlite-devel

OpenSuse
--------

The zlib development package should be installed:

.. code-block:: console

   # zypper install zlib-devel

To use the system's pcre2 libraries, add the pcre2 development package:

.. code-block:: console

   # zypper install pcre2-devel

If database support is needed the package mysql-devel and/or postgresql-devel will
need to be installed.

.. code-block:: console

   # zypper install postgresql-devel mysql-devel

Debian
------

.. warning::

   The Debian instructions are probably out of date. Contributions updating this section
   would be appreciated.


Debian has replaced bash with dash, and this may cause issues during
installation. Dash does not appear to support all of the features
available in other shells, and may display an error when trying to set
the server's IP address on an agent system. The error can be ignored,
but the server ip address will need to be set.

Do this by making sure something like the following information is in
the agent's ossec.conf:

.. code-block:: console

   <ossec_config>
     <client>
       <server-ip>SERVER'S IP</server-ip>
     </client>

This can also be avoided by using bash to run ``install.sh``:

.. code-block:: console

   # bash ./install.sh


