=========
Downloads
=========


+--------------+-----------------------------------------------+-------+
| latest development snapshots                                         |
+==============+===============================================+=======+
| server/agent | https://github.com/ossec/ossec-hids                   |
+--------------+-----------------------------------------------+-------+
| web ui       | https://github.com/ossec/ossec-wui                    |
+--------------+-----------------------------------------------+-------+
| docs         | https://github.com/ossec/ossec-docs                   |
+--------------+-----------------------------------------------+-------+
| Latest Stable Release (2.8.1)                                        |
+--------------+-----------------------------------------------+-------+
| Server/Agent | https://github.com/ossec/ossec-hids           | CRC   |
+--------------+-----------------------------------------------+-------+
| Agent Windows| https://github.com/ossec/ossec-wui            | CRC   |
+--------------+-----------------------------------------------+-------+
| Virtual Appl | https://github.com/ossec/ossec-docs           | CRC   |
+--------------+-----------------------------------------------+-------+

RPMs for RHEL, CentOS, Fedora and others
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Available in the `AtomiCorp repository <http://www5.atomicorp.com/channels/ossec/>`_.

+-------------------------------------------------------------------------------------------+
| CentOS                                                                                    |
+==============+============================================================================+
| el5          | `i386 <http://www5.atomicorp.com/channels/ossec/centos/5/i386/RPMS/>`_     |
+--------------+----------------------------------------------------------------------------+
| el5          | `x86_64 <http://www5.atomicorp.com/channels/ossec/centos/5/x86_64/RPMS/>`_ |
+--------------+----------------------------------------------------------------------------+
| el6          | `i386 <http://www5.atomicorp.com/channels/ossec/centos/5/i386/RPMS/>`_     |
+--------------+----------------------------------------------------------------------------+
| el6          | `x86_64 <http://www5.atomicorp.com/channels/ossec/centos/6/x86_64/RPMS/>`_ |
+--------------+----------------------------------------------------------------------------+

+-------------------------------------------------------------------------------------------+
| Fedora                                                                                    |
+==============+============================================================================+
| el5          | `i386 <http://www5.atomicorp.com/channels/ossec/fedora/20/i386/RPMS/>`_    |
+--------------+----------------------------------------------------------------------------+
| el5          | `x86_64 <http://www5.atomicorp.com/channels/ossec/fedora/5/x86_64/RPMS/>`_ |
+--------------+----------------------------------------------------------------------------+
| el6          | `i386 <http://www5.atomicorp.com/channels/ossec/fedora/5/i386/RPMS/>`_     |
+--------------+----------------------------------------------------------------------------+
| el6          | `x86_64 <http://www5.atomicorp.com/channels/ossec/fedora/6/x86_64/RPMS/>`_ |
+--------------+----------------------------------------------------------------------------+
| All          | `6 - 20 <http://www5.atomicorp.com/channels/ossec/fedora/>`_               |
+--------------+----------------------------------------------------------------------------+

DEBs for Debian Wheezy, Jessie and Sid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Available in the `AlienVault repository <http://ossec.alienvault.com/repos/apt/debian/pool/main/o/>`_.


+-------------------------------------------------------------------------------------------+
| Debian                                                                                    |
+==============+============================================================================+
| OSSEC Server | `Wheezy, Jessie, Sid <http://ossec.alienvault.com/repos/apt/debian/pool/main/o/ossec-hids/>`_ |
+--------------+----------------------------------------------------------------------------+
| OSSEC Agent  | `Wheezy, Jessie, Sid <http://ossec.alienvault.com/repos/apt/debian/pool/main/o/ossec-hids-agent/>`_ |
+--------------+----------------------------------------------------------------------------+



RPM Installation
================

To install with yum do the following:

.. code:: console

    # wget -q -O – https://www.atomicorp.com/installers/atomic | sh
    # yum install ossec-hids ossec-hids-server (or ossec-hids-client for the agent)


DEB Installation
================

To install with apt-get do the following:

.. code:: console 

    # wget -O – http://ossec.alienvault.com/repos/apt/conf/ossec-key.gpg.key | apt-key add –
    # echo “deb http://ossec.alienvault.com/repos/apt/debian wheezy main” >> /etc/apt/sources.list
    (change wheezy for your Debian distribution)
    # apt-get update
    # apt-get install ossec-hids  (or ossec-hids-agent)

PGP key
=======

Before you install any package from our project, we recommend that you
verify it using our PGP key. Follow these two steps if you are not used
to using gpg. You first need to import our public key:

.. code:: console

    ossec-test# wget http://www.ossec.net/files/OSSEC-PGP-KEY.asc
    ossec-test# gpg –import OSSEC-PGP-KEY.asc

And then verify each file against its signature:

.. code:: console

    ossec-test# gpg –verify file.sig file

You should get the following result:


.. code:: console

    gpg: Signature made Tue 19 Jul 2011 03:13:58 PM BRT using RSA key ID A3901351
    gpg: Good signature from “Daniel B. Cid ”
    Primary key fingerprint: 6F11 9E06 487A AF17 C84C E48A 456B 17CF A390 1351

Note that the key expiration date was changed lately. If you get an
warning saying “gpg: Note: This key has expired!”, make sure to update
the key and run the “import” command again (as specified above).

Contribute back!
----------------

If you find ossec useful and would like to contribute back to the
community, please contact us. We have a lot of work to do and any help
is appreciated.
