.. _install_source:

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


1. Download the latest version and verify its GPG signature (see below).

2. Verify the requirements listed in :ref:`install_req` are installed or available.

   .. versionadded: 3.3

      PCRE2 is a new requirement, and manual installation is required.

   .. versionadded: 3.5

      The default compilation process assumes the development package for PCRE2 is installed.

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


Verify the tarball signature
============================

Release tarballs are signed with a GPG key. The detached signature file (``.asc``)
is published alongside each release on `GitHub Releases <https://github.com/ossec/ossec-hids/releases>`_
and on `https://www.ossec.net/download-ossec/ <https://www.ossec.net/download-ossec/>`_.

Import the signing key from the official OSSEC site (do not rely on keyservers;
``gpg --recv-key`` may fail for this key with a "contains no user ID" error):

.. code-block:: console

   curl -O https://www.ossec.net/files/OSSEC-ARCHIVE-KEY.asc
   gpg --import OSSEC-ARCHIVE-KEY.asc

Download the tarball and matching signature for the release you are installing.
Replace ``VERSION`` with the release tag (for example ``4.1.0``):

.. code-block:: console

   curl -LO https://github.com/ossec/ossec-hids/releases/download/VERSION/ossec-hids-VERSION.tar.gz
   curl -LO https://github.com/ossec/ossec-hids/releases/download/VERSION/ossec-hids-VERSION.tar.gz.asc
   gpg --verify ossec-hids-VERSION.tar.gz.asc ossec-hids-VERSION.tar.gz

A successful verification prints ``Good signature`` from
``Scott R. Shinn <scott@atomicorp.com>``. GPG may also warn that the key is
not certified with a trusted signature until you assign trust locally; that
warning is expected on a first import.

The signing key fingerprint is:

.. code-block:: console

   B50F B194 7A0A E311 45D0  5FAD EE1B 0E6B 2D83 87B7

Only proceed with ``install.sh`` or ``make install`` after the signature verifies.
See also :ref:`faq_gpg_verify`.
