=========
Downloads
=========

Source Downloads
~~~~~~~~~~~~~~~~

+--------------+-----------------------------------------------+-------------+
| Latest development snapshots                                               |
+==============+===============================================+=============+
| Server/Agent | https://github.com/ossec/ossec-hids/releases                |
+--------------+-----------------------------------------------+-------------+
| Web UI       | https://github.com/ossec/ossec-wui/releases                 |
+--------------+-----------------------------------------------+-------------+
| Docs         | https://github.com/ossec/ossec-docs                         |
+--------------+-----------------------------------------------+-------------+

+---------------------+-----------------------------------------------+--------------------------+----------------+
| Latest Stable Release (2.9.0)                                       | Checksum                 | Signature      |
+=====================+===============================================+==========================+================+
| Server/Agent Unix   | `ossec-hids-2.9.1.tar.gz`_ – `Release Notes`_ |                          | `GPG Unix`_    |      
+---------------------+-----------------------------------------------+--------------------------+----------------+
| Agent Windows       | `ossec-agent-win32-2.9.0.exe`_                |                          | `GPG Windows`_ |
+---------------------+-----------------------------------------------+--------------------------+----------------+
| Virtual Appliance   | `ossec-vm-2.8.3.ova`_ – `README`_             | `VA Checksum`_           |                |
+---------------------+-----------------------------------------------+--------------------------+----------------+
| Docker Container    | `wazuh/docker-ossec`_                         |                          |                |
+---------------------+-----------------------------------------------+--------------------------+----------------+

.. _ossec-hids-2.9.1.tar.gz: https://github.com/ossec/ossec-hids/archive/2.9.1.tar.gz
.. _Release Notes: https://github.com/ossec/ossec-hids/releases/tag/2.9.1
.. _GPG Unix: https://github.com/ossec/ossec-hids/releases/download/2.9.1/ossec-hids-2.9.1.tar.gz.asc
.. _ossec-agent-win32-2.9.0.exe: https://updates.atomicorp.com/channels/atomic/windows/ossec-agent-win32-2.9.0-1738.exe
.. _GPG Windows: https://updates.atomicorp.com/channels/atomic/windows/ossec-agent-win32-2.9.0-1738.exe.asc
.. _ossec-vm-2.8.3.ova: http://ossec.wazuh.com/vm/ossec-vm-2.8.3.ova
.. _README: http://ossec.wazuh.com/vm/ossec-vm-2.8.3.README
.. _VA Checksum: http://ossec.wazuh.com/vm/ossec-vm-2.8.3-checksum.txt
.. _wazuh/docker-ossec: https://hub.docker.com/r/wazuh/docker-ossec/


RHEL, CentOS, Fedora and others
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Available in the `Atomicorp repository <https://updates.atomicorp.com/channels/atomic/>`_.

+-----------------------------------------------------------------------------------------------------+---------------------------------------------------+
| CentOS / Redhat / Amazon Linux                                                                      |  atomic-release                                   |
+=================+===================================================================================+===================================================+
| el5 i386        | `<https://updates.atomicorp.com/channels/atomic/centos/5/i386/RPMS/>`_            | `atomic-release-1.0-21.el5.art.noarch.rpm`_       |
+-----------------+-----------------------------------------------------------------------------------+---------------------------------------------------+
| el5 x86_64      | `<https://updates.atomicorp.com/channels/atomic/centos/5/x86_64/RPMS/>`_          | `atomic-release-1.0-21.el5.art.noarch.rpm`_       |
+-----------------+-----------------------------------------------------------------------------------+---------------------------------------------------+
| el6 i386        | `<https://updates.atomicorp.com/channels/atomic/centos/6/i386/RPMS/>`_            | `atomic-release-1.0-21.el6.art.noarch.rpm`_       |
+-----------------+-----------------------------------------------------------------------------------+---------------------------------------------------+
| el6 x86_64      | `<https://updates.atomicorp.com/channels/atomic/centos/6/x86_64/RPMS/>`_          | `atomic-release-1.0-21.el6.art.noarch.rpm`_       |
+-----------------+-----------------------------------------------------------------------------------+---------------------------------------------------+
| el7 x86_64      | `<https://updates.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/>`_          | `atomic-release-1.0-21.el7.art.noarch.rpm`_       |
+-----------------+-----------------------------------------------------------------------------------+---------------------------------------------------+

Note: Amazon Linux users are recommended to use the EL6 x86_64 repository

+------------------------------------------------------------------------------------------------------+------------------------------------------------------+
| Fedora                                                                                               | atomic-release                                       |
+==================+===================================================================================+======================================================+
| fc24 x86_64      | `<https://updates.atomicorp.com/channels/atomic/fedora/24/x86_64/RPMS/>`_         | `atomic-release-1.0-21.fc24.art.noarch.rpm`_         |
+------------------+-----------------------------------------------------------------------------------+------------------------------------------------------+
| fc25 x86_64      | `<https://updates.atomicorp.com/channels/atomic/fedora/25/x86_64/RPMS/>`_         | `atomic-release-1.0-21.fc25.art.noarch.rpm`_         |
+------------------+-----------------------------------------------------------------------------------+------------------------------------------------------+
| fc26 x86_64      | `<https://updates.atomicorp.com/channels/atomic/fedora/26/x86_64/RPMS/>`_         | `atomic-release-1.0-21.fc26.art.noarch.rpm`_         |
+------------------+-----------------------------------------------------------------------------------+------------------------------------------------------+
| Legacy           | `<https://updates.atomicorp.com/channels/atomic/fedora/>`_                        |                                                      |
+------------------+-----------------------------------------------------------------------------------+------------------------------------------------------+

.. _atomic-release-1.0-21.el5.art.noarch.rpm: https://updates.atomicorp.com/channels/atomic/centos/5/i386/RPMS/atomic-release-1.0-21.el5.art.noarch.rpm
.. _atomic-release-1.0-21.el6.art.noarch.rpm: https://updates.atomicorp.com/channels/atomic/centos/6/i386/RPMS/atomic-release-1.0-21.el6.art.noarch.rpm
.. _atomic-release-1.0-21.el7.art.noarch.rpm: https://updates.atomicorp.com/channels/atomic/centos/7/x86_64/RPMS/atomic-release-1.0-21.el7.art.noarch.rpm
.. _atomic-release-1.0-21.fc24.art.noarch.rpm: https://updates.atomicorp.com/channels/atomic/fedora/24/x86_64/RPMS/atomic-release-1.0-21.fc24.art.noarch.rpm
.. _atomic-release-1.0-21.fc25.art.noarch.rpm: https://updates.atomicorp.com/channels/atomic/fedora/25/x86_64/RPMS/atomic-release-1.0-21.fc25.art.noarch.rpm
.. _atomic-release-1.0-21.fc26.art.noarch.rpm: https://updates.atomicorp.com/channels/atomic/fedora/26/x86_64/RPMS/atomic-release-1.0-21.fc26.art.noarch.rpm


Ubuntu, and Debian and others
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------+
| Ubuntu                                                                                |
+==============+========================================================================+
| 12 (precise) | `<https://updates.atomicorp.com/channels/ossec/ubuntu/pool/main/o/>`_  | 
+--------------+------------------------------------------------------------------------+
| 14 (trusty)  | `<https://updates.atomicorp.com/channels/ossec/ubuntu/pool/main/o/>`_  | 
+--------------+------------------------------------------------------------------------+
| 16 (xenial)  | `<https://updates.atomicorp.com/channels/ossec/ubuntu/pool/main/o/>`_  | 
+--------------+------------------------------------------------------------------------+


+---------------------------------------------------------------------------------------+
| Debian                                                                                |
+==============+========================================================================+
| 7 (wheezy)   | `<https://updates.atomicorp.com/channels/ossec/debian/pool/main/o/>`_  | 
+--------------+------------------------------------------------------------------------+
| 8 (jessie)   | `<https://updates.atomicorp.com/channels/ossec/debian/pool/main/o/>`_  | 
+--------------+------------------------------------------------------------------------+





Yum/DNF Automated Installation on Centos, Redhat, or Fedora
================

Automated installer:

.. code:: console

    
     # Add Yum repo configuration
     wget -q -O - https://updates.atomicorp.com/installers/atomic | sudo bash
    
     # Server
     sudo yum install ossec-hids-server 

     # Agent
     sudo yum install ossec-hids-agent




Manual Yum/DNF installation on Centos, Redhat, Amazon Linux or Fedora
================

1. Download the atomic-release file for your distribution

2. Install the atomic-relase package (Note: This includes the OSSEC GPG key)

.. code:: console

   sudo rpm -Uvh atomic-release*rpm

3. Install ossec package

.. code:: console

   # Server
   sudo yum install ossec-hids server

   # Agent
   sudo yum install ossec-hids-agent



APT Automated Installation on Ubuntu and Debian
===============

.. code:: console

    # Add Apt sources.lst
    wget -q -O - https://updates.atomicorp.com/installers/atomic | sudo bash

    # Server 
    apt-get install ossec-hids-server 

    # Agent
    apt-get install ossec-hids-agent


Manual APT Installation on Ubuntu and Debian
===============

1. Add the GPG key

.. code:: console

        wget -q -O - https://www.atomicorp.com/RPM-GPG-KEY.art.txt  | sudo apt-key add -

2. Add the repo configuration to sources.list

.. code:: console

        source /etc/lsb-release

        # Ubuntu
        echo "deb https://updates.atomicorp.com/channels/atomic/ubuntu $DISTRIB_CODENAME main" >>  /etc/apt/sources.list.d/atomic.list

        # Debian
        echo "deb https://updates.atomicorp.com/channels/atomic/debian $DISTRIB_CODENAME main" >>  /etc/apt/sources.list.d/atomic.list

GPG / PGP key
~~~~~~~

+-----------------------+-----------------------------------------------------+
| Key                   | Manual Download Link                                |
+-----------------------+-----------------------------------------------------+
| OSSEC-ARCHIVE-KEY.asc | https://ossec.github.io/files/OSSEC-ARCHIVE-KEY.asc |
+-----------------------+-----------------------------------------------------+
| OSSEC-PGP-KEY.asc     | https://ossec.github.io/files/OSSEC-PGP-KEY.asc     |
+-----------------------+-----------------------------------------------------+
| RPM-GPG-KEY.art.txt   | https://www.atomicorp.com/RPM-GPG-KEY.art.txt       |
+-----------------------+-----------------------------------------------------+

Before you install any package from our project, we recommend that you
verify it using our PGP key. Follow these two steps if you are not used
to using gpg. You first need to import our public key:

.. code:: console

    # wget https://ossec.github.io/files/OSSEC-ARCHIVE-KEY.asc
    # gpg --import OSSEC-ARCHIVE-KEY.asc

And then verify each file against its signature:

.. code:: console

    ossec-test# gpg --verify file.asc 

You should get the following result:


.. code:: console

    gpg: Signature made Tue 20 Dec 2016 11:35:58 AM EST using RSA key ID 2D8387B7
    gpg: Good signature from "Scott R. Shinn <scott@atomicorp.com>"
    Primary key fingerprint: B50F B194 7A0A E311 45D0  5FAD EE1B 0E6B 2D83 87B7


Note that the signing key was changed in December 2016. The previous signing key
"6F11 9E06 487A AF17 C84C E48A 456B 17CF A390 1351" has expired. If you get an warning 
saying “gpg: Note: This key has expired!”, make sure to update the key and run the 
“import” command again (as specified above).


Presentation Slides
~~~~~~~~~~~~~~~~~~~

Several of the OSSEC Project Team members have presented at conferences. 
Here is a collection of materials from some of those presentations.

+----------------------------------------------------------------------+
| `Decoding AWS CloudTrail with OSSEC`_                                |
+----------------------------------------------------------------------+
| `Log Analysis Using OSSEC`_                                          |
+----------------------------------------------------------------------+
| `Making the Most of OSSEC`_                                          |
+----------------------------------------------------------------------+
| `Malware Detection with OSSEC`_                                      |
+----------------------------------------------------------------------+
| `Open Source Security`_                                              |
+----------------------------------------------------------------------+
| `OSSEC Active Response and Self Healing`_                            |
+----------------------------------------------------------------------+
| `OSSEC and OSSIM Unified Open Source Security`_                      |
+----------------------------------------------------------------------+
| `OSSEC at Scale`_                                                    |
+----------------------------------------------------------------------+
| `OSSEC Con 2012 Day 1`_                                              |
+----------------------------------------------------------------------+
| `OSSEC Con 2012 Day 2`_                                              |
+----------------------------------------------------------------------+
| `OSSEC Log Management with Elasticsearch`_                           |
+----------------------------------------------------------------------+
| `OSSEC PCI Solution 2.0`_                                            |
+----------------------------------------------------------------------+
 
.. _Decoding AWS CloudTrail with OSSEC: https://bintray.com/artifact/download/ossec/ossec-presentations/Decoding_AWS_CloudTrail_with_OSSEC.pptx
.. _Log Analysis Using OSSEC: https://bintray.com/artifact/download/ossec/ossec-presentations/Log_Analysis_using_OSSEC.pdf
.. _Making the Most of OSSEC: https://bintray.com/artifact/download/ossec/ossec-presentations/Making_the_Most_of_OSSEC.pdf 
.. _Malware Detection with OSSEC: https://bintray.com/artifact/download/ossec/ossec-presentations/Malware_Detection_with_OSSEC.pptx
.. _Open Source Security: https://bintray.com/artifact/download/ossec/ossec-presentations/OpenSourceSecurity_2013.pptx
.. _OSSEC Active Response and Self Healing: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_Active_Response_and_Self_Healing.pdf
.. _OSSEC and OSSIM Unified Open Source Security: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_and_OSSIM_Unified_Open_Source_Security.pdf
.. _OSSEC at Scale: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_at_Scale.pdf
.. _OSSEC Con 2012 Day 1: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_Con_2012-day-1.pdf
.. _OSSEC Con 2012 Day 2: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_Con_2012-day-2.pdf
.. _OSSEC Log Management with Elasticsearch: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_Log_Mangement_with_Elasticsearch.pptx
.. _OSSEC PCI Solution 2.0: https://bintray.com/artifact/download/ossec/ossec-presentations/OSSEC_PCI_Solution_2.0.pdf

Contribute back!
~~~~~~~~~~~~~~~~

If you find ossec useful and would like to contribute back to the
community, please contact us. We have a lot of work to do and any help
is appreciated.


|
