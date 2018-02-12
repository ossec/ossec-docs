
.. _install_req:

Installations requirements
==========================

For UNIX systems, OSSEC only requires gnu make, gcc, and libc.
OpenSSL is a suggested, but optional, prerequisite. 
However, you always have the option to pre-compile
it on one system and move the binaries to the final box.

Ubuntu
------

On Ubuntu you will need the *build-essential* package in order to
compile and install OSSEC.

To install the package run the following command.

.. code-block:: console

    # apt-get install build-essential


If database support is needed *mysql-dev* or *postgresql-dev* should be
installed. Run the following command to install these packages.

.. code-block:: console 

    # apt-get install mysql-dev postgresql-dev

To use the SQLite features, the `libsqlite3-dev` package is necessary.

.. code-block:: console

   # apt-get install libsqlite3-dev

RedHat
------

RedHat should have all packages needed by default, but if database
support is needed the package mysql-devel and/or postgresql-devel will
need to be installed.

.. code-block:: console

    # yum install mysql-devel postgresql-devel

To use the SQLite features, the `sqlite-devel` package is necessary.

.. code-block:: console

   # yum install sqlite-devel


Debian
------

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


