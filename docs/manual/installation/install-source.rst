.. _install:

Manager/Agent Installation
==========================


Installation of OSSEC HIDS is very simple, the ``install.sh`` shell script automating most of it.
There are a few questions to be answered before the installation will occur, one of the most 
important being which type of installation is desired.
It is important to choose the correct installation type: server, agent, local, or hybrid.
More information on them can be found on the `OSSEC Architecture page <../ossec-architecture.html>`_.

.. note::

    In the following installation the commands follow the ``#``. 
    Everything else is either comments or output. 


1. Download the latest version and verify its signature. Github releases may change the actual
   tarball downloads, so a checksum isn't a great way to verify it.

2. Verify the requirements listed in :ref:`install_req` are installed or available.

3. Extract the compressed package and run the ``install.sh`` script. It will guide you 
   through the installation and compile the source (not shown).

    .. code-block:: console 

        # tar -zxvf ossec-hids-*.tar.gz (or gunzip -d; tar -xvf)
        # cd ossec-hids-* 
        # ./install.sh

4. The OSSEC manager listens on UDP port 1514. Any firewalls between the agents and 
   the manager will need to allow this traffic.

5. The server, agent, and hybrid installations will require additional configuration. 
   More information can be found on the `Managing the agents page <../agent/agent-management.html>`_.

6. Start OSSEC HIDS by running the following command:

    .. code-block:: console 

        # /var/ossec/bin/ossec-control start  


Manual Installation
===================

OSSEC can also be installed in a more manual fashion.
No modifications will be made to the `ossec.conf` file, so it will have to be configured after installation.
The `ossec`, `ossecm` and `ossecr` users will still be created automatically.

After the source tarball is downloaded and extracted:

.. code-block:: console

   cd ossec-hids-*/src
   make TARGET=<server|local|agent>
   make install

Build options can still be passed to `make` (`USE_ZEROMQ`, `USE_GEOIP`, etc.).

