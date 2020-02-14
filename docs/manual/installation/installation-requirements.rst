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

PCRE2 support has been added to OSSEC v3.3. The build system can either use the system's PCRE2 libraries,
or the necessary bits can be built as part of the installation process.

.. versionadded:: 3.4

As of v3.4 the default build process has set `PCRE2_SYSTEM`, and expects pcre2 to be installed on the system.
On many Linux systems the necessary packages would be `dev` or `devel` packages specifically.

Alternatively, OSSEC can build and use pcre2 without installing the packages.
To do this the `pcre2-10.32` sources must be installed in `src/external`:

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

At a minimum, the following packages should be installed:

.. code-block:: console

   apt-get install build-essential make zlib1g-dev libpcre2-dev

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

At a minimum, the following packages should be installed:

.. code-block:: console

   yum install zlib-devel pcre2-devel make gcc

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

FreeBSD
-------

If you want to build and install OSSEC on FreeBSD you can work together with
its `FreeBSD Ports Collection <https://www.freebsd.org/ports>`_.

There you can find and setup **ossec-hids-agent**, **ossec-hids-local** or
**ossec-hids-server**.

If you want to build and install only the the required dependencies to run an
OSSEC server/manager, without installing it:

.. code-block:: console

   # cd /usr/ports/security/ossec-hids-server
   # make

If you want to install this particular port, you should run ``make install``.

FreeBSD also offers pre-compiled packages for OSSEC and all its dependencies. If you
want to install them you must work with
`pkg <https://www.freebsd.org/doc/handbook/pkgng-intro.html>`_.

OpenBSD
-------

As OpenBSD also has its own `OpenBSD Ports Collection <https://www.openbsd.org/faq/ports/ports.html>`_,
you can build and install OSSEC using it if you want.

It only offers **security/ossec-hids**, so:

.. code-block:: console

   # cd /usr/ports/security/ossec-hids
   # make

Just like the previous example with FreeBSD, if you want to install it all (not just the
dependencies) you must run ``make install`` instead. Another option would be using
`pkg_add <https://www.openbsd.org/faq/faq15.html>`_.

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


